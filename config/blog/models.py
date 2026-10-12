from django.db import models


class Number_image(models.Model):
    title = models.CharField(max_length=130, verbose_name="sarlavha matni")
    photo = models.ImageField(upload_to="bot_photos/", verbose_name="rasm")
    caption = models.TextField(blank=True, null=True, verbose_name="rasm tagidagi matn")
    javob = models.CharField(max_length=75, verbose_name="to'g'ri javob")
    yuborilgan = models.BooleanField(default=False, verbose_name="yuborilganmi")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bot xabari"


class Postbutton(models.Model):
    post = models.ForeignKey(Number_image, on_delete=models.CASCADE, related_name="buttons")
    text = models.CharField(max_length=75, verbose_name="tugma matni")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Post tugmasi"

class CaptchaFoydalanuvchi(models.Model):
    chat_id = models.CharField(max_length=50)
    ism = models.CharField(max_length=100, blank=True)
    togri_son = models.IntegerField(null=True, blank=True)
    holat = models.CharField(max_length=30, default='ism_kutilmoqda')


    def __str__(self):
        return self.chat_id












































# from django.db import models
#
# # Create your models here.
#
#
# class Number_image(models.Model):
#     title = models.CharField(max_length=130, verbose_name = "sarlafha matni")
#     photo = models.ImageField(upload_to = "bot_photos/", verbose_name="rasm")
#     caption = models.TextField(blank=True, null=True, verbose_name= "rasm tagidagi matn")
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#         # verbose_name = "bot habarlari"
#
#     class Meta:
#         verbose_name = "Bot xabari"
#
# class Postbutton(models.Model):
#     post = models.ForeignKey(Number_image, on_delete=models.CASCADE, related_name = "buttons")
#     text = models.CharField(max_length = 75, verbose_name = "tugma matn")
#     # urls = model.URLField(verbose_name = "tugma havolasi")
#
#     def __str__(self):
#         return self.text

    class Meta:
        verbose_name = "Post tugmasi"






























































# from django.db import models
#
#
# class TelegramGroup(models.Model):
#     TURI_CHOICES = [
#         ('guruh', "Guruh"),
#         ('kanal', "Kanal"),
#     ]
#
#     nomi = models.CharField(max_length=100)
#     chat_id = models.CharField(max_length=50, unique=True)
#     turi = models.CharField(max_length=10, choices=TURI_CHOICES, default='guruh')
#
#     def __str__(self):
#         return f"{self.nomi} ({self.get_turi_display()})"
#
#
#
# class BroadcastLog(models.Model):
#     chat_id = models.CharField(max_length=50)
#     message_id = models.CharField(max_length=50, blank=True, null=True)
#     text = models.TextField(blank=True)
#     has_photo = models.BooleanField(default=False)
#     success = models.BooleanField(default=False)
#     response = models.JSONField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         holat = "OK" if self.success else "FAIL"
#         return f"{self.chat_id} - {holat} - {self.created_at:%Y-%m-%d %H:%M}"
#
#     class Meta:
#         verbose_name = "Xabar jurnali"
#         ordering = ['-created_at']
#
#
# class MessageReply(models.Model):
#     original_message = models.ForeignKey(
#         BroadcastLog, on_delete=models.SET_NULL, null=True, blank=True,
#         related_name='javoblar'
#     )
#     chat_id = models.CharField(max_length=50)
#     from_user_id = models.CharField(max_length=50, blank=True)
#     from_user_name = models.CharField(max_length=150, blank=True)
#     reply_text = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.from_user_name} - {self.created_at:%Y-%m-%d %H:%M}"
#
#     class Meta:
#         verbose_name = "Xabarga javob"
#         ordering = ['-created_at']
#
#
# class CaptchaFoydalanuvchi(models.Model):
#     HOLAT_CHOICES = [
#         ('ism_kutilmoqda', "Ism kutilmoqda"),
#         ('captcha_kutilmoqda', "Captcha kutilmoqda"),
#         ('tasdiqlandi', "Tasdiqlandi"),
#     ]
#
#     chat_id = models.CharField(max_length=50, unique=True)
#     ism = models.CharField(max_length=100, blank=True)
#     togri_son = models.IntegerField(null=True, blank=True)
#     holat = models.CharField(max_length=20, choices=HOLAT_CHOICES, default='ism_kutilmoqda')
#     yaratilgan_vaqt = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.ism} - {self.get_holat_display()}"
#
#     class Meta:
#         verbose_name = "Captcha foydalanuvchi"
#         ordering = ['-yaratilgan_vaqt']