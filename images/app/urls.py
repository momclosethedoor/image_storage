from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', index),
    path('images/load', load_image, name='img_load'),
    path('images/api', csrf_exempt(image_api), name='img_load_api'),
    path('<key_url>', get_img)
]