from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

root = Path(__file__).resolve().parent
iconset = root / 'icon.iconset'
iconset.mkdir(parents=True, exist_ok=True)

size = 1024
img = Image.new('RGBA', (size, size), '#111111')
draw = ImageDraw.Draw(img)

margin = 70
draw.rounded_rectangle((margin, margin, size - margin, size - margin), radius=180, fill='#202020', outline='#f5a623', width=18)

cx, cy = size // 2, size // 2
ring = 270
draw.ellipse((cx - ring, cy - ring, cx + ring, cy + ring), outline='#f5a623', width=30)
draw.line((cx, cy, cx, cy - 145), fill='#f5a623', width=24)
draw.line((cx, cy, cx + 110, cy + 85), fill='#ffffff', width=20)

try:
    font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 240)
except Exception:
    font = ImageFont.load_default()

text = 'Q'
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
draw.text((cx - text_width // 2, cy + 120 - text_height // 2), text, font=font, fill='#ffffff')

img.save(root / 'icon-1024.png')
img.resize((512, 512), Image.Resampling.LANCZOS).save(root / 'icon.png')

for icon_size in [16, 32, 64, 128, 256, 512, 1024]:
    resized = img.resize((icon_size, icon_size), Image.Resampling.LANCZOS)
    if icon_size == 16:
        resized.save(iconset / 'icon_16x16.png')
    if icon_size == 32:
        resized.save(iconset / 'icon_16x16@2x.png')
        resized.save(iconset / 'icon_32x32.png')
    if icon_size == 64:
        resized.save(iconset / 'icon_32x32@2x.png')
    if icon_size == 128:
        resized.save(iconset / 'icon_128x128.png')
    if icon_size == 256:
        resized.save(iconset / 'icon_128x128@2x.png')
        resized.save(iconset / 'icon_256x256.png')
    if icon_size == 512:
        resized.save(iconset / 'icon_256x256@2x.png')
        resized.save(iconset / 'icon_512x512.png')
    if icon_size == 1024:
        resized.save(iconset / 'icon_512x512@2x.png')

img.save(root / 'icon.ico', format='ICO', sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

print('Icon assets generated')
