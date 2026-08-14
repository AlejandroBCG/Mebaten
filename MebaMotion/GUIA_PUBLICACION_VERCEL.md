# Publicación en Vercel

Este proyecto está preparado para publicarse en Vercel como sitio estático con una función serverless en `/api/cotizacion`.

## Variables de entorno necesarias

Configura estas variables en Vercel > Project Settings > Environment Variables:

- `QUOTE_TO`: `alex.bglez97@gmail.com`
- `SMTP_HOST`: por ejemplo `smtp.gmail.com`
- `SMTP_PORT`: `587`
- `SMTP_USER`: correo remitente
- `SMTP_PASS`: contraseña de aplicación del correo remitente
- `SMTP_FROM`: correo remitente
- `SMTP_TLS`: `true`

Si usas Gmail, activa verificación en dos pasos y crea una contraseña de aplicación.

## Dominio comprado en Wix

1. Agrega tu dominio en Vercel > Project > Settings > Domains.
2. Vercel te mostrará los registros DNS requeridos.
3. En Wix > Domains > Manage DNS Records, apunta:
   - Dominio raíz con el A record indicado por Vercel.
   - `www` con el CNAME indicado por Vercel.
4. Espera la propagación y el certificado SSL automático.

El dominio seguirá viéndose como el dominio comprado en Wix; Wix solo administrará el DNS.
