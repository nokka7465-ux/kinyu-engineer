"""Generate Open Graph image (1200x630) matching the site's brand.
Output: og-image.png at repo root.
Run: python scripts/gen_og_image.py
"""
from PIL import Image, ImageDraw, ImageFont
import os, random

W, H = 1200, 630
BG = (245, 240, 232)        # --bg
ACCENT = (26, 58, 42)       # --accent (深緑)
ACCENT2 = (196, 87, 42)     # --accent2 (オレンジ)
TEXT = (28, 26, 22)         # --text
TEXT2 = (92, 86, 72)        # --text2
TEXT3 = (156, 144, 128)     # --text3

FONT_DIR = 'C:/Windows/Fonts'
NOTO_SERIF = os.path.join(FONT_DIR, 'NotoSerifJP-VF.ttf')
NOTO_SANS = os.path.join(FONT_DIR, 'NotoSansJP-VF.ttf')

img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)

# Subtle noise
random.seed(42)
for _ in range(2200):
    x = random.randint(0, W); y = random.randint(0, H)
    a = random.randint(8, 18)
    d.point((x, y), (max(0, BG[0]-a), max(0, BG[1]-a), max(0, BG[2]-a)))

# Top-left label
label_font = ImageFont.truetype(NOTO_SANS, 22)
d.text((80, 70), 'REAL STORY  /  実体験ブログ', font=label_font, fill=ACCENT2)
d.rectangle([80, 110, 220, 112], fill=ACCENT2)

# Main title (2 lines)
title_font = ImageFont.truetype(NOTO_SERIF, 96)
d.text((80, 165), '金融マンが', font=title_font, fill=ACCENT)
d.text((80, 285), 'エンジニアになった話。', font=title_font, fill=ACCENT)

# Accent bar + subtitle
d.rectangle([80, 425, 86, 485], fill=ACCENT2)
sub_font = ImageFont.truetype(NOTO_SERIF, 28)
d.text((110, 422), '異業種転職の実体験を、', font=sub_font, fill=TEXT2)
d.text((110, 458), '包み隠さず書くブログ。', font=sub_font, fill=TEXT2)

# Bottom row
auth_font = ImageFont.truetype(NOTO_SANS, 22)
url_font = ImageFont.truetype(NOTO_SANS, 18)
meta_font = ImageFont.truetype(NOTO_SANS, 16)

# Bottom-left
d.text((80, 555), 'by  tamal', font=auth_font, fill=TEXT)

# Bottom center divider dots
center_font = ImageFont.truetype(NOTO_SANS, 14)
d.text((80, 590), '35 articles  ·  1.8yr engineer  ·  個人事業主', font=center_font, fill=TEXT3)

# Bottom-right URL
url_text = 'kinyu-engineer.github.io'
bbox = d.textbbox((0, 0), url_text, font=url_font)
url_w = bbox[2] - bbox[0]
d.text((W - 80 - url_w, 558), url_text, font=url_font, fill=TEXT3)

# Right-edge thin accent line for visual balance
d.rectangle([W - 12, 0, W - 8, H], fill=ACCENT2)

out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'og-image.png')
img.save(out, 'PNG', optimize=True)
print(f'Saved {out} ({os.path.getsize(out)} bytes)')
