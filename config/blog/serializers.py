from rest_framework import serializers
from .models import Number_image, Postbutton


class PostButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postbutton
        fields = ['id', 'text']


class NumberImageSerializer(serializers.ModelSerializer):
    buttons = PostButtonSerializer(many=True)

    class Meta:
        model = Number_image
        fields = ['id', 'title', 'photo', 'caption', 'javob', 'yuborilgan', 'buttons']
        read_only_fields = ['yuborilgan']

    def create(self, validated_data):
        tugmalar_data = validated_data.pop('buttons')
        post = Number_image.objects.create(**validated_data)
        for tugma in tugmalar_data:
            Postbutton.objects.create(post=post, **tugma)
        return post















# from rest_framework import serializers
#
#
# class BroadcastSerializer(serializers.Serializer):
#     text = serializers.CharField(required=False, allow_blank=True)
#     photo = serializers.ImageField(required=False)
#     target = serializers.ChoiceField(
#         choices=['groups', 'channels', 'all'],
#         default='all',
#     )
#
#     def validate(self, data):
#         if not data.get('text') and not data.get('photo'):
#             raise serializers.ValidationError(
#                 "text yoki photo dan kamida bittasi bo'lishi shart."
#             )
#         return data