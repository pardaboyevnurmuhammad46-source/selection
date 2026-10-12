from django.urls import path
from .views import NumberImageCreateView

urlpatterns = [
    path('api/post-yaratish/', NumberImageCreateView.as_view())
]

