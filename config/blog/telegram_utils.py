import json
import requests
from django.conf import settings
from .models import CaptchaFoydalanuvchi


def postni_botga_yuborish(post):
    token = settings.TELEGRAM_BOT_TOKEN
    foydalanuvchilar = CaptchaFoydalanuvchi.objects.filter(holat='tasdiqlandi')

    tugmalar_qatori = []
    qator = []
    for i, tugma in enumerate(post.buttons.all(), start=1):
        qator.append({"text": tugma.text, "callback_data": f"post_javob_{post.id}_{tugma.id}"})
        if i % 3 == 0:
            tugmalar_qatori.append(qator)
            qator = []
    if qator:
        tugmalar_qatori.append(qator)

    reply_markup = {"inline_keyboard": tugmalar_qatori}

    for foydalanuvchi in foydalanuvchilar:
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        with post.photo.open('rb') as rasm:
            data = {
                "chat_id": foydalanuvchi.chat_id,
                "caption": f"{post.title}\n\n{post.caption or ''}",
                "reply_markup": json.dumps(reply_markup),
            }
            files = {"photo": rasm}
            requests.post(url, data=data, files=files, timeout=10)

    post.yuborilgan = True
    post.save()