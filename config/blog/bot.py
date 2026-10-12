import os
import sys
import time
import json
import random
import django
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.conf import settings
from blog.models import Number_image, Postbutton

token = settings.TELEGRAM_BOT_TOKEN


def answer_callback(callback_query_id, text=None):
    url = f"https://api.telegram.org/bot{token}/answerCallbackQuery"
    data = {"callback_query_id": callback_query_id}
    if text:
        data["text"] = text
    requests.post(url, data=data, timeout=5)


def send_text(chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data, timeout=5)


def send_post(chat_id):
    post = Number_image.objects.order_by('?').first()

    if not post:
        send_text(chat_id, "Hozircha postlar mavjud emas.")
        return

    tugmalar_qatori = []
    for tugma in post.buttons.all():
        tugmalar_qatori.append(
            {"text": tugma.text, "callback_data": f"post_javob_{post.id}_{tugma.id}"}
        )

    tugmalar = {"inline_keyboard": [tugmalar_qatori]} if tugmalar_qatori else None

    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    data = {"chat_id": chat_id}
    if post.caption:
        data["caption"] = post.caption
    if tugmalar:
        data["reply_markup"] = json.dumps(tugmalar)

    files = {"photo": post.photo.open("rb")}
    requests.post(url, data=data, files=files, timeout=10)


def handle_private_message(chat_id, text):
    if text == "/start":
        send_post(chat_id)
        return


def handle_callback(callback):
    chat_id = str(callback["message"]["chat"]["id"])
    callback_id = callback["id"]
    data = callback["data"]

    if data.startswith("post_javob_"):
        qismlar = data.split("_")
        post_id = qismlar[2]
        tugma_id = qismlar[3]
        try:
            post = Number_image.objects.get(id=post_id)
            tugma = Postbutton.objects.get(id=tugma_id, post=post)
        except (Number_image.DoesNotExist, Postbutton.DoesNotExist):
            answer_callback(callback_id, "Xatolik")
            return

        if tugma.text == post.javob:
            answer_callback(callback_id, "To'g'ri! ✅")
        else:
            answer_callback(callback_id, "Noto'g'ri ❌")


def run_bot():
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    print("telegram bot ishga tushdi")
    offset = None

    while True:
        try:
            params = {"timeout": 30, "offset": offset}
            response = requests.get(url, params=params, timeout=35).json()

            for result in response.get("result", []):
                offset = result["update_id"] + 1

                if "callback_query" in result:
                    handle_callback(result["callback_query"])
                    continue

                message = result.get("message")
                if not message:
                    continue

                chat = message["chat"]
                chat_id = str(chat["id"])
                chat_type = chat.get("type")
                text = message.get("text", "")

                if chat_type == "private":
                    handle_private_message(chat_id, text)

        except requests.exceptions.RequestException as e:
            print(f"Tarmoq xatosi: {e}")
            time.sleep(3)

        time.sleep(1)


if __name__ == "__main__":
    run_bot()