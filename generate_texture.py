"""
Script para generar la textura del circuito de linea negra.
Ejecutar: python3 generate_texture.py
Genera: line_track.png (512x512 px)
"""

try:
    from PIL import Image, ImageDraw
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "--break-system-packages", "-q"])
    from PIL import Image, ImageDraw

import os

SIZE = 512
img = Image.new("RGB", (SIZE, SIZE), color=(200, 200, 200))  # fondo gris claro
draw = ImageDraw.Draw(img)

# Dibujar pista circular (ovalo)
LINE_WIDTH = 28
MARGIN = 80

# Rectangulo exterior con esquinas redondeadas simuladas por ellipses + rectangulos
cx, cy = SIZE // 2, SIZE // 2
rx, ry = SIZE // 2 - MARGIN, SIZE // 2 - MARGIN

# Dibujar ovalo negro
draw.ellipse(
    [cx - rx, cy - ry, cx + rx, cy + ry],
    outline=(20, 20, 20),
    width=LINE_WIDTH
)

# Linea de largada (blanco/negro)
for i in range(8):
    color = (0, 0, 0) if i % 2 == 0 else (255, 255, 255)
    draw.rectangle(
        [cx - 4 + i * 8, cy - ry - LINE_WIDTH // 2,
         cx - 4 + i * 8 + 8, cy - ry + LINE_WIDTH // 2],
        fill=color
    )

output = os.path.join(os.path.dirname(__file__), "..", "worlds", "line_track.png")
img.save(output)
print(f"Textura generada: {os.path.abspath(output)}")
