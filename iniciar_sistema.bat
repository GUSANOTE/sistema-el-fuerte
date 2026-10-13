@echo off
title Sistema El Fuerte - Ferreteria
chcp 65001 > nul
echo ========================================================
echo   Iniciando Sistema de Gestion - Ferreteria EL FUERTE
echo ========================================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python no está instalado o no se encuentra en el PATH.
    echo Por favor instale Python 3.10 o superior desde https://www.python.org/
    echo Asegúrese de marcar la casilla "Add python.exe to PATH".
    echo.
    pause
    exit /b 1
)

if not exist venv (
    echo [1/3] Creando entorno virtual (venv)...
    python -m venv venv
)

echo [2/3] Verificando dependencias necesarias...
call .\venv\Scripts\activate.bat
pip install -r requirements.txt

echo [3/3] Verificando base de datos...
python manage.py migrate --noinput

echo.
echo ========================================================
echo   ¡Todo listo! Iniciando servidor y abriendo navegador.
echo   URL: http://127.0.0.1:8000/
echo   Usuario: admin
echo   Contraseña: admin
echo ========================================================
echo.
timeout /t 2 > nul
start http://127.0.0.1:8000/
python manage.py runserver 127.0.0.1:8000
pause
