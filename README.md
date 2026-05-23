# 🤖 Proyecto Webots — Seguidor de Línea

## Estructura del proyecto

```
webots_project/
├── worlds/
│   ├── line_follower.wbt   ← Mundo principal (ABRIR ESTE)
│   └── line_track.png      ← Textura del circuito
├── controllers/
│   └── line_follower/
│       └── line_follower.py  ← Controlador Python del robot
└── README.md
```

## ¿Cómo abrirlo?

1. Abre **Webots** (versión R2023b o superior recomendada)
2. Ve a `File → Open World`
3. Selecciona el archivo: `worlds/line_follower.wbt`
4. Presiona ▶ **Play** y observa al robot seguir la línea

## ¿Qué hace el robot?

- Es un **E-puck** con 3 sensores de suelo infrarrojos
- Sigue una **línea negra** en forma de óvalo
- Lógica de control:

| Sensor | Detección | Acción |
|--------|-----------|--------|
| Centro | Línea negra | Avanza recto |
| Derecha | Línea negra | Gira a la derecha |
| Izquierda | Línea negra | Gira a la izquierda |
| Ninguno | Sin línea | Gira buscando |

## Requisitos

- Webots R2023b: https://cyberbotics.com
- Python 3.8+

## Personalización rápida

En `controllers/line_follower/line_follower.py`:
- `BASE_SPEED` → velocidad del robot (0–6.28)
- `LINE_THRESHOLD` → sensibilidad de detección (0–1000)
