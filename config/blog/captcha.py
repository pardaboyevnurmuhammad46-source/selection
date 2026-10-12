import random
import io
from PIL import Image, ImageDraw, ImageFont


def son_yarat():
    return random.randint(1000, 9999)


def captcha_rasm_yasash(son):
    kenglik = 300
    balandlik = 120

    rasm = Image.new("RGB", (kenglik, balandlik), color=(240, 240, 240))
    chizuvchi = ImageDraw.Draw(rasm)

    try:
        shrift = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50
        )
    except OSError:
        shrift = ImageFont.load_default()

    i = 0
    while i < 8:
        x1 = random.randint(0, kenglik)
        y1 = random.randint(0, balandlik)
        x2 = random.randint(0, kenglik)
        y2 = random.randint(0, balandlik)
        chizuvchi.line((x1, y1, x2, y2), fill=(180, 180, 180), width=2)
        i += 1

    matn = str(son)
    matn_kutisi = chizuvchi.textbbox((0, 0), matn, font=shrift)
    matn_kengligi = matn_kutisi[2] - matn_kutisi[0]
    matn_balandligi = matn_kutisi[3] - matn_kutisi[1]

    x = (kenglik - matn_kengligi) // 2
    y = (balandlik - matn_balandligi) // 2

    chizuvchi.text((x, y), matn, font=shrift, fill=(20, 20, 20))

    j = 0
    while j < 100:
        x = random.randint(0, kenglik)
        y = random.randint(0, balandlik)
        chizuvchi.point((x, y), fill=(120, 120, 120))
        j += 1

    buffer = io.BytesIO()
    buffer.name = "captcha.png"
    rasm.save(buffer, "PNG")
    buffer.seek(0)
    return buffer