import os
import asyncio
from celery import shared_task
from django.conf import settings
from aiogram import Bot
from aiogram.types import FSInputFile

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)


async def _send_broadcast(chat_ids, text, photo_path):
    for chat_id in chat_ids:
        try:
            if photo_path and os.path.exists(photo_path):
                photo = FSInputFile(photo_path)
                await bot.send_photo(chat_id=chat_id, photo=photo, caption=text)
            else:
                await bot.send_message(chat_id=chat_id, text=text)

            await asyncio.sleep(0.05)
        except Exception as e:
            print(f"Chat ID: {chat_id} ga xabar yuborishda xatolik: {e}")


@shared_task
def send_broadcast_task(chat_ids, text, photo_path=None):
    asyncio.run(_send_broadcast(chat_ids, text, photo_path))
    if photo_path and os.path.exists(photo_path):
        try:
            os.remove(photo_path)
        except Exception as e:
            print(f"Vaqtinchalik faylni o'chirishda xatolik: {e}")





from celery import shared_task
from .telegram_utils import postni_botga_yuborish as yuborish_funksiyasi


@shared_task
def postni_yuborish_task(post_id):
    from .models import Number_image
    try:
        post = Number_image.objects.get(id=post_id)
    except Number_image.DoesNotExist:
        return
    yuborish_funksiyasi(post)