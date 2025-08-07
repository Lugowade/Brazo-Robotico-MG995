@echo off
REM Instala pygame y pyserial (si ya están instalados, solo mostrará que ya están presentes)
C:\Users\eduar\AppData\Local\Programs\Python\Python313\python.exe -m pip install --upgrade pip
C:\Users\eduar\AppData\Local\Programs\Python\Python313\python.exe -m pip install pygame pyserial

REM Ejecuta el script de control de joycon
C:\Users\eduar\AppData\Local\Programs\Python\Python313\python.exe joycon_to_esp32.py

pause
