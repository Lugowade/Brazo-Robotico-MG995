Brazo Robótico de 6 Ejes con ESP32 y Joystick – MG995  
**Autor**: Luis (lugowade)  
**Plataforma**: ESP32 + Python + Joystick  
**Servomotores**: 6 × MG995  
**Licencia**: MIT

## 📦 Contenido del Repositorio

├── ejecutar.py          # Script Python para controlar el brazo desde PC  
├── instalar.ino         # Código para el ESP32 (Arduino IDE)  
├── README.md            # Instrucciones de uso

## ⚙️ Requisitos

🧰 Hardware:
- 1 × ESP32 (cualquier modelo con pines PWM)
- 6 × Servomotores MG995
- 1 × Fuente externa 5V (mínimo 2A, preferible 5A)
- 1 × Mando/Joystick (Xbox, PS4, etc.)
- 1 × PC con Windows o Linux
- Cables jumper
- (Opcional) Condensador de 1000µF entre VCC y GND

💻 Software:
- Python 3.8+
- Arduino IDE
- Librerías Python:

  pip install pygame pyserial

## ⚡ Diagrama de Conexión

| Servo | Pin ESP32 |
|-------|-----------|
| S0    | GPIO 13   |
| S1    | GPIO 12   |
| S2    | GPIO 33   |
| S3    | GPIO 27   |
| S4    | GPIO 26   |
| S5    | GPIO 25   |

⚠️ Importante:
- Los MG995 NO deben alimentarse desde el ESP32.
- Usa una fuente externa de 5V/2A (o más).
- Conecta TODOS los GND: ESP32, fuente y servos.

## 🔧 Instalación

1. Abre `instalar.ino` en el Arduino IDE.
2. Selecciona la placa ESP32 correcta.
3. Sube el código al ESP32 por USB.
4. Conecta los servos a los pines según la tabla.
5. Usa fuente externa de 5V para alimentar los servos.
6. Conecta el joystick al PC.
7. Asegúrate de tener Python instalado y ejecuta:

   pip install pygame pyserial

## ▶️ Ejecución

1. Verifica el puerto COM del ESP32:
   - Windows: Administrador de dispositivos > Puertos
   - Linux: `ls /dev/ttyUSB*` o `ls /dev/ttyACM*`

2. Edita el archivo `ejecutar.py` y cambia la línea:

   ESP32_PORT = 'COM3'

3. Ejecuta el script desde consola:

   python ejecutar.py

## 🎮 Controles del Joystick

| Acción                   | Botón / Eje        |
|--------------------------|--------------------|
| Base y articulaciones    | Joysticks izquierdo y derecho |
| Rotar muñeca             | B (↻) / X (↺)       |
| Cerrar garra             | ZL (cerrar lento)  |
| Abrir garra              | ZR (abrir rápido)  |
| Reiniciar todos los servos | START (+)        |
| Apagar y salir del programa | SELECT (-)      |

## 🛠️ Consejos de seguridad

- Inicia el brazo en posición neutral.
- No fuerces los servos en posiciones físicas extremas.
- Revisa polaridad de fuente antes de conectar.

## ❓ Problemas comunes

- Joystick no detectado: verifica drivers o reemplaza control.
- ESP32 no responde: revisa puerto COM y conexión USB.
- Servos vibran o se reinician: usa una fuente de mayor corriente (mínimo 2A o más).

## 💡 Personalización

- Control remoto con WiFi o Bluetooth
- Grabación y reproducción de movimientos
- Interfaz gráfica (Tkinter o PyQt)
- Control desde celular

## ✅ Créditos

Proyecto desarrollado por **Luis (lugowade)**  
Distribuido bajo la licencia **MIT**.

## 🧾 Licencia (MIT)

MIT License

Copyright (c) 2025 Luis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
