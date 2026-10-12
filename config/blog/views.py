from rest_framework import generics
from .models import Number_image
from .serializers import NumberImageSerializer
from .telegram_utils import postni_botga_yuborish


class NumberImageCreateView(generics.CreateAPIView):
    queryset = Number_image.objects.all()
    serializer_class = NumberImageSerializer

    def perform_create(self, serializer):
        post = serializer.save()
        postni_botga_yuborish(post)













# import os
# import tempfile
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
#
# from .models import TelegramGroup
# from .serializers import BroadcastSerializer
# from .tasks import send_broadcast_task
#
#
# class BroadcastView(APIView):
#     parser_classes = [MultiPartParser, FormParser, JSONParser]
#
#     def post(self, request):
#         serializer = BroadcastSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         text = serializer.validated_data.get('text')
#         photo = serializer.validated_data.get('photo')
#         target = serializer.validated_data.get('target')
#
#         # 1. Guruh va kanallarni saralash
#         guruhlar = TelegramGroup.objects.all()
#         if target == 'groups':
#             guruhlar = guruhlar.filter(turi='guruh')
#         elif target == 'channels':
#             guruhlar = guruhlar.filter(turi='kanal')
#
#         chat_ids = list(guruhlar.values_list('chat_id', flat=True))
#         if not chat_ids:
#             return Response(
#                 {"detail": f"'{target}' bo'yicha hech qanday guruh/kanal topilmadi."},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#
#         # 2. Agar rasm yuklangan bo'lsa, vaqtinchalik diskka saqlash
#         photo_path = None
#         if photo:
#             suffix = os.path.splitext(photo.name)[1] or ".jpg"
#             tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
#             for chunk in photo.chunks():
#                 tmp.write(chunk)
#             tmp.close()
#             photo_path = tmp.name
#
#         # 3. Celery vazifasiga uzatish (photo_path qo'shildi)
#         send_broadcast_task.delay(
#             chat_ids=chat_ids,
#             text=text,
#             photo_path=photo_path
#         )
#
#         return Response(
#             {"detail": f"{len(chat_ids)} ta ({target}) manzilga yuborish navbatga qo'yildi."},
#             status=status.HTTP_200_OK
#         )