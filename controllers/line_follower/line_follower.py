"""
Controlador: Seguidor de Linea
Robot: E-puck
Descripcion: El robot sigue una linea negra usando 3 sensores de suelo.

Logica:
  - gs0 (derecha), gs1 (centro), gs2 (izquierda)
  - Valor alto = suelo claro (fuera de la linea)
  - Valor bajo  = suelo oscuro (sobre la linea)

Velocidades:
  - Si linea al centro  -> avanza recto
  - Si linea a la derecha -> gira derecha
  - Si linea a la izquierda -> gira izquierda
"""

from controller import Robot

# Constantes
TIME_STEP = 8
MAX_SPEED = 6.28   # rad/s (velocidad maxima del e-puck)
BASE_SPEED = 4.0   # velocidad de crucero

# Umbral: por debajo de este valor el sensor detecta linea negra
LINE_THRESHOLD = 500

def run_robot():
    robot = Robot()

    # Inicializar motores
    left_motor  = robot.getDevice("left wheel motor")
    right_motor = robot.getDevice("right wheel motor")
    left_motor.setPosition(float("inf"))
    right_motor.setPosition(float("inf"))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Inicializar sensores de suelo
    gs = []
    for name in ["gs0", "gs1", "gs2"]:
        sensor = robot.getDevice(name)
        sensor.enable(TIME_STEP)
        gs.append(sensor)

    print("=== Seguidor de Linea Iniciado ===")
    print("gs0=derecha | gs1=centro | gs2=izquierda")

    step = 0
    while robot.step(TIME_STEP) != -1:
        # Leer sensores
        gs_val = [sensor.getValue() for sensor in gs]

        gs0 = gs_val[0]  # derecha
        gs1 = gs_val[1]  # centro
        gs2 = gs_val[2]  # izquierda

        # Detectar linea
        on_line_right  = gs0 < LINE_THRESHOLD
        on_line_center = gs1 < LINE_THRESHOLD
        on_line_left   = gs2 < LINE_THRESHOLD

        # Logica de control
        if on_line_center and not on_line_right and not on_line_left:
            # Linea al centro -> avanza recto
            left_speed  = BASE_SPEED
            right_speed = BASE_SPEED

        elif on_line_right and not on_line_left:
            # Linea a la derecha -> girar derecha
            left_speed  = BASE_SPEED
            right_speed = BASE_SPEED * 0.2

        elif on_line_left and not on_line_right:
            # Linea a la izquierda -> girar izquierda
            left_speed  = BASE_SPEED * 0.2
            right_speed = BASE_SPEED

        elif on_line_right and on_line_left:
            # Linea en ambos lados (cruce) -> avanza recto
            left_speed  = BASE_SPEED
            right_speed = BASE_SPEED

        else:
            # Sin linea detectada -> buscar girando suavemente
            left_speed  = BASE_SPEED * 0.5
            right_speed = BASE_SPEED * -0.5

        # Aplicar velocidades (clamp)
        left_speed  = max(-MAX_SPEED, min(MAX_SPEED, left_speed))
        right_speed = max(-MAX_SPEED, min(MAX_SPEED, right_speed))

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

        # Log cada 100 pasos
        if step % 100 == 0:
            print(f"Paso {step:5d} | gs=[{gs0:.0f},{gs1:.0f},{gs2:.0f}] | "
                  f"v=({left_speed:.2f},{right_speed:.2f})")
        step += 1

if __name__ == "__main__":
    run_robot()
