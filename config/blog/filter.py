import django_filters
from .models import Number_image, Postbutton, CaptchaFoydalanuvchi


class Number_imageFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    javob = django_filters.CharFilter(field_name='javob', lookup_expr='icontains')

    class Meta:
        model = Number_image
        fields = ['title', 'javob']



class postbuttonFilter(django_filters.FilterSet):
    text = django_filters.TextField(lookup_expr='icontains')

    class Meta:
        model = Postbutton
        fields = []


class CaptchaFoydalanuvchiFilter(django_filters.FilterSet):
    chat_id = django_filters.CharFilter(field_name='chat_id', lookup_expr='icontains')
    togri_son = django_filters.CharFilter(field_name='togri_son', lookup_expr='icontains')
    ism = django_filters.CharFilter(field_name='ism', lookup_expr='icontains')

    class Meta:
        model = CaptchaFoydalanuvchi
        fields = ['chat_id', 'togri_son', 'ism']

