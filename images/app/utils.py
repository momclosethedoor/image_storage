from string import ascii_uppercase, ascii_lowercase, digits
import random
from .models import *
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from PIL import Image

def gen_key(length: int)-> str:
    key = ''.join(random.choices(ascii_uppercase + digits + ascii_lowercase, k=length))
    return key

def gen_link(request) -> str:
    link = ''
    img = request.FILES["image"]
    try:
        img_obj = Images.objects.get(img=img)
        link = request.build_absolute_uri(f'/{img_obj.key}')
    except ObjectDoesNotExist:
        key = gen_key(6)
        try:
            img_obj, _ = Images.objects.get_or_create(img=img, key=key)
            link = request.build_absolute_uri(f'/{img_obj.key}')
        except IntegrityError:
            gen_link(request)
    return link, img_obj.img.url

def get_img_by_key(key):
    try:
        img_obj = Images.objects.get(key=key)
    except ObjectDoesNotExist:
        return None
    return img_obj.img
