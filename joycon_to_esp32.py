import pygame
import serial
import time
import sys

ESP32_PORT = 'COM3'
BAUD_RATE = 115200
DEADZONE = 0.4
DELAY_BETWEEN_COMMANDS = 0.01
LOOP_DELAY = 0.01
SMOOTH_STEP = 2
FAST_STEP = 4

wrist_angle = 90
garra_angulo = 90
servo_memory = [90, 90, 90, 90]
last_sent_angles = [None] * 6

def map_axis(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def apply_deadzone(value, threshold=DEADZONE):
    return 0 if abs(value) < threshold else value

def smooth_move(current, target, step=SMOOTH_STEP):
    if abs(target - current) <= step:
        return target
    return current + step if target > current else current - step

try:
    esp32 = serial.Serial(ESP32_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
except Exception as e:
    sys.exit(1)

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    sys.exit(1)

joystick = pygame.joystick.Joystick(0)
joystick.init()

try:
    while True:
        pygame.event.pump()

        lx = apply_deadzone(joystick.get_axis(0))
        ly = apply_deadzone(joystick.get_axis(1))
        rx = apply_deadzone(joystick.get_axis(2))
        ry = apply_deadzone(joystick.get_axis(3))

        joystick_values = [lx, ly, rx, ry]
        servo_angles = []

        for i in range(4):
            if joystick_values[i] == 0:
                angle = servo_memory[i]
            else:
                target_angle = map_axis(joystick_values[i], -1, 1, 0, 180)
                angle = smooth_move(servo_memory[i], target_angle, step=FAST_STEP)
                servo_memory[i] = angle
            servo_angles.append(angle)

        boton_b = joystick.get_button(1)
        boton_x = joystick.get_button(2)

        if boton_b:
            wrist_angle += SMOOTH_STEP
        if boton_x:
            wrist_angle -= SMOOTH_STEP
        wrist_angle = max(0, min(180, wrist_angle))
        servo_angles.append(wrist_angle)

        boton_zl = joystick.get_button(6)
        boton_zr = joystick.get_button(7)

        if boton_zl:
            garra_angulo = smooth_move(garra_angulo, 0, step=1)
        elif boton_zr:
            garra_angulo = 90

        servo_angles.append(garra_angulo)

        if joystick.get_button(7):
            target_angles = [90, 90, 90, 90, 90, 90]
            current_angles = servo_memory + [wrist_angle, garra_angulo]
            for _ in range(45):
                for i in range(6):
                    current_angles[i] = smooth_move(current_angles[i], target_angles[i], step=2)
                    comando = f"S{i}:{int(current_angles[i])}\n"
                    esp32.write(comando.encode())
                    time.sleep(DELAY_BETWEEN_COMMANDS)
                time.sleep(0.01)
            servo_memory = [90, 90, 90, 90]
            wrist_angle = 90
            garra_angulo = 90
            last_sent_angles = [None] * 6
            time.sleep(0.3)

        if joystick.get_button(6):
            for i in range(6):
                comando = f"S{i}:90\n"
                esp32.write(comando.encode())
                time.sleep(DELAY_BETWEEN_COMMANDS)
            break

        for i, angulo in enumerate(servo_angles):
            if last_sent_angles[i] != int(angulo):
                comando = f"S{i}:{int(angulo)}\n"
                esp32.write(comando.encode())
                last_sent_angles[i] = int(angulo)
                time.sleep(DELAY_BETWEEN_COMMANDS)

        time.sleep(LOOP_DELAY)

except KeyboardInterrupt:
    pass
finally:
    esp32.close()
    pygame.quit()
