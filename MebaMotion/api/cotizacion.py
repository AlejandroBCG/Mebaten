from __future__ import annotations

import json
import os
import smtplib
from email.message import EmailMessage
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler


TO_EMAIL = os.getenv("QUOTE_TO", "alex.bglez97@gmail.com")


def smtp_configured() -> bool:
    return bool(os.getenv("SMTP_HOST") and os.getenv("SMTP_USER") and os.getenv("SMTP_PASS"))


def make_body(fields: dict[str, str]) -> str:
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
        value = fields.get(key) or "No especificado"
        lines.append(f"{label}: {value}")
    return "\n".join(lines)


def validate(fields: dict[str, str]) -> None:
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


def send_email(fields: dict[str, str]) -> None:
    if not smtp_configured():
        raise RuntimeError("SMTP no configurado en Vercel.")

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
    msg.set_content(make_body(fields))

    with smtplib.SMTP(host, port, timeout=20) as smtp:
        if use_tls:
            smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(msg)


class handler(BaseHTTPRequestHandler):
    def send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Accept")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_json(HTTPStatus.NO_CONTENT, {})

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length).decode("utf-8")
            fields = json.loads(raw or "{}")
            if not isinstance(fields, dict):
                raise ValueError("Solicitud inválida.")

            validate(fields)
            send_email(fields)
            self.send_json(HTTPStatus.OK, {
                "ok": True,
                "email_sent": True,
                "message": "Solicitud enviada. Un asesor comercial te contactará pronto.",
            })
        except ValueError as exc:
            self.send_json(HTTPStatus.BAD_REQUEST, {"ok": False, "message": str(exc)})
        except Exception as exc:
            self.send_json(HTTPStatus.INTERNAL_SERVER_ERROR, {
                "ok": False,
                "message": f"No pudimos enviar la solicitud por correo: {exc}",
            })
