from __future__ import annotations

import json
import os
import secrets
import smtplib
from datetime import datetime
from email.message import EmailMessage
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SUBMISSIONS_DIR = ROOT / "solicitudes"
TO_EMAIL = os.getenv("QUOTE_TO", "alex.bglez97@gmail.com")


def json_response(handler: SimpleHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type, Accept")
    handler.end_headers()
    handler.wfile.write(body)


def validate_fields(fields: dict[str, str]) -> None:
    if fields.get("_gotcha"):
        raise ValueError("Solicitud descartada.")

    required = {
        "name": "Nombre",
        "phone": "Teléfono",
        "email": "Correo",
        "location": "Ciudad / Estado",
        "equipment": "Qué necesitas cotizar",
        "message": "Cuéntanos qué necesitas",
    }
    missing = [label for key, label in required.items() if not str(fields.get(key, "")).strip()]
    if missing:
        raise ValueError("Faltan campos obligatorios: " + ", ".join(missing))

    email = str(fields.get("email", ""))
    if "@" not in email or "." not in email.split("@")[-1]:
        raise ValueError("El correo no parece válido.")


def submission_text(fields: dict[str, str]) -> str:
    labels = [
        ("name", "Nombre"),
        ("company", "Empresa"),
        ("phone", "Teléfono"),
        ("email", "Correo"),
        ("location", "Ciudad / Estado"),
        ("equipment", "Equipo solicitado"),
        ("message", "Mensaje"),
    ]
    lines = ["Nueva solicitud de cotización desde mebaten.com", ""]
    for key, label in labels:
        lines.append(f"{label}: {fields.get(key) or 'No especificado'}")
    return "\n".join(lines)


def save_submission(fields: dict[str, str]) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    folder = SUBMISSIONS_DIR / f"{stamp}-{secrets.token_hex(3)}"
    folder.mkdir(parents=True, exist_ok=False)
    data = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "to_email": TO_EMAIL,
        "fields": {key: value for key, value in fields.items() if key != "_gotcha"},
    }
    (folder / "datos.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return folder


def smtp_configured() -> bool:
    return bool(os.getenv("SMTP_HOST") and os.getenv("SMTP_USER") and os.getenv("SMTP_PASS"))


def send_email(fields: dict[str, str]) -> None:
    host = os.getenv("SMTP_HOST", "")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER", "")
    password = os.getenv("SMTP_PASS", "")
    sender = os.getenv("SMTP_FROM", user)
    use_tls = os.getenv("SMTP_TLS", "true").lower() not in {"0", "false", "no"}

    msg = EmailMessage()
    msg["Subject"] = f"Solicitud de cotización Mebaten - {fields.get('equipment', 'Proyecto')}"
    msg["From"] = sender
    msg["To"] = TO_EMAIL
    msg["Reply-To"] = fields.get("email", sender)
    msg.set_content(submission_text(fields))

    with smtplib.SMTP(host, port, timeout=20) as smtp:
        if use_tls:
            smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)


class MebatenHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_OPTIONS(self) -> None:
        json_response(self, HTTPStatus.NO_CONTENT, {})

    def do_POST(self) -> None:
        if self.path != "/api/cotizacion":
            json_response(self, HTTPStatus.NOT_FOUND, {"ok": False, "message": "Endpoint no encontrado."})
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(content_length).decode("utf-8")
            fields = json.loads(body or "{}")
            validate_fields(fields)
            folder = save_submission(fields)

            if smtp_configured():
                send_email(fields)
                message = "Solicitud enviada. Un asesor comercial te contactará pronto."
                email_sent = True
            else:
                message = "Solicitud guardada localmente. Configura SMTP para enviarla por correo."
                email_sent = False

            json_response(self, HTTPStatus.OK, {
                "ok": True,
                "email_sent": email_sent,
                "saved_to": str(folder),
                "message": message,
            })
        except ValueError as exc:
            json_response(self, HTTPStatus.BAD_REQUEST, {"ok": False, "message": str(exc)})
        except Exception as exc:
            json_response(self, HTTPStatus.INTERNAL_SERVER_ERROR, {"ok": False, "message": f"Error del servidor: {exc}"})


def main() -> int:
    if "--check" in os.sys.argv:
        print(f"Proyecto: {ROOT}")
        print(f"Destino: {TO_EMAIL}")
        print(f"SMTP configurado: {'sí' if smtp_configured() else 'no'}")
        return 0

    port = int(os.getenv("PORT", "8000"))
    server = ThreadingHTTPServer(("0.0.0.0", port), MebatenHandler)
    print(f"Servidor Mebaten activo en http://localhost:{port}")
    print(f"Formulario: http://localhost:{port}/api/cotizacion")
    print(f"Correo destino: {TO_EMAIL}")
    if not smtp_configured():
        print("SMTP no configurado: las solicitudes se guardarán en la carpeta 'solicitudes'.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
