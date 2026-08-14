@echo off
setlocal
cd /d "%~dp0"

set "PORT=8000"
set "QUOTE_TO=alex.bglez97@gmail.com"

REM Para enviar correos reales, configura SMTP antes de iniciar.
REM En Gmail necesitas una contraseña de aplicación, no tu contraseña normal.
REM set "SMTP_HOST=smtp.gmail.com"
REM set "SMTP_PORT=587"
REM set "SMTP_USER=tu_correo@gmail.com"
REM set "SMTP_PASS=tu_contrasena_de_aplicacion"
REM set "SMTP_FROM=tu_correo@gmail.com"

set "PYTHON_EXE=C:\Users\LENOVO\AppData\Local\Python\bin\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=C:\Users\LENOVO\AppData\Local\Microsoft\WindowsApps\python.exe"

echo Iniciando servidor de cotizaciones Mebaten...
echo Sitio: http://localhost:%PORT%
echo Endpoint: http://localhost:%PORT%/api/cotizacion
echo Destino configurado: %QUOTE_TO%
echo.
"%PYTHON_EXE%" server.py
pause
