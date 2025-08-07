@echo off
echo Instalando dependencias para el control del brazo con JoyCons...

REM Verificar si Python y pip están instalados
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python no está instalado o no está en el PATH.
    echo Descargalo desde https://www.python.org/downloads/
    pause
    exit /b
)

REM Instalar pygame y pyserial
echo Instalando pygame y pyserial...
python -m pip install --upgrade pip
python -m pip install pygame pyserial

echo.
echo ✅ Instalación completada.
echo Puedes ejecutar ahora el script Python: joycon_to_esp32.py
pause
