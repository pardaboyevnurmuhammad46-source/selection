from django.contrib import admin
from .models import Number_image, Postbutton
from .tasks import postni_yuborish_task


class PostButtonInline(admin.TabularInline):
    model = Postbutton
    extra = 1
    fields = ('text',)


def postni_yuborish(modeladmin, request, queryset):
    for post in queryset:
        postni_yuborish_task.delay(post.id)

postni_yuborish.short_description = "Tanlangan postlarni botga yuborish"


@admin.register(Number_image)
class NumberImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'javob', 'yuborilgan', 'created_at')
    search_fields = ('title', 'caption')
    list_filter = ('created_at', 'yuborilgan')
    inlines = [PostButtonInline]
    actions = [postni_yuborish]


@admin.register(Postbutton)
class PostButtonAdmin(admin.ModelAdmin):
    list_display = ('text', 'post')
    search_fields = ('text',)










# from django.contrib import admin
# from .models import Number_image, Postbutton
#
#
# class PostButtonInline(admin.TabularInline):
#     model = Postbutton
#     extra = 1  #
#     fields = ('text', 'url')
#
#
# @admin.register(Number_image)
# class NumberImageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title', 'caption')
#     list_filter = ('created_at',)
#     inlines = [PostButtonInline]
#
#
# @admin.register(Postbutton)
# class PostButtonAdmin(admin.ModelAdmin):
#     list_display = ('text', 'post', 'url')
#     search_fields = ('text', 'url')


































#
# from django.contrib import admin
# from .models import (
#     TelegramGroup,
#     BroadcastLog,
#     MessageReply,
#     CaptchaFoydalanuvchi,
# )
#
#
# @admin.register(TelegramGroup)
# class TelegramGroupAdmin(admin.ModelAdmin):
#     list_display = ['nomi', 'chat_id', 'turi']
#     list_filter = ['turi']
#     search_fields = ['nomi', 'chat_id']
#
#
# # @admin.register(TugilganKun)
# # class TugilganKunAdmin(admin.ModelAdmin):
# #     list_display = ['ism', 'tugilgan_sana', 'holat', 'faol', 'chat_id', 'qoshilgan_vaqt']
# #     list_filter = ['holat', 'faol']
# #     search_fields = ['ism', 'chat_id']
#
#
# @admin.register(BroadcastLog)
# class BroadcastLogAdmin(admin.ModelAdmin):
#     list_display = ['chat_id', 'success', 'has_photo', 'created_at']
#     list_filter = ['success', 'has_photo']
#     search_fields = ['chat_id', 'text']
#
#
# @admin.register(MessageReply)
# class MessageReplyAdmin(admin.ModelAdmin):
#     list_display = ['from_user_name', 'gurux_nomi', 'qaysi_habarga', 'reply_text', 'created_at']
#     list_filter = ['created_at']
#     search_fields = ['from_user_name', 'reply_text']
#     readonly_fields = ['gurux_nomi', 'qaysi_habarga', 'from_user_name', 'reply_text', 'created_at']
#     fields = ['gurux_nomi', 'qaysi_habarga', 'from_user_name', 'reply_text', 'created_at']
#
#     def has_add_permission(self, request):
#         return False
#
#     def gurux_nomi(self, obj):
#         gurux = TelegramGroup.objects.filter(chat_id=obj.chat_id).first()
#         return gurux.nomi if gurux else "—"
#     gurux_nomi.short_description = "Guruh nomi"
#
#     def qaysi_habarga(self, obj):
#         if obj.original_message and obj.original_message.text:
#             matn = obj.original_message.text
#             return matn[:60] + "..." if len(matn) > 60 else matn
#         return "Topilmadi"
#     qaysi_habarga.short_description = "Qaysi xabarga javob"
#
#
# @admin.register(CaptchaFoydalanuvchi)
# class CaptchaFoydalanuvchiAdmin(admin.ModelAdmin):
#     list_display = ['ism', 'chat_id', 'holat', 'yaratilgan_vaqt']
#     list_filter = ['holat']
#     search_fields = ['ism', 'chat_id']