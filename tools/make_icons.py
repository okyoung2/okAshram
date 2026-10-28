"""런처와 앱 타일 아이콘(PNG)을 생성한다.  실행: python tools/make_icons.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = "C:/Windows/Fonts/NirmalaB.ttf"


def glyph_icon(char, bg, fg, size, out, scale=0.62, radius=0.0):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * radius), fill=bg)
    font = ImageFont.truetype(FONT, int(size * scale))
    l, t, r, b = d.textbbox((0, 0), char, font=font)
    d.text(((size - (r - l)) / 2 - l, (size - (b - t)) / 2 - t), char, font=font, fill=fg)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)


# 런처(okAshram) 아이콘: 홈 화면용, maskable 대응을 위해 글자를 작게 둔다
for s in (192, 512):
    glyph_icon("ॐ", "#1b1712", "#e0a83c", s, ROOT / f"icons/icon-{s}.png", scale=0.5)

# 앱 타일 아이콘
glyph_icon("अ", "#7a2e2e", "#ffffff", 256, ROOT / "icons/sanskrit.png", radius=0.22)
glyph_icon("த", "#b4532a", "#ffffff", 256, ROOT / "icons/tamil.png", radius=0.22)
