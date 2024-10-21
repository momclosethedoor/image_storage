from django.shortcuts import redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponseNotFound
from django.template.response import TemplateResponse
from django.urls.exceptions import NoReverseMatch
from .models import ImageForm

from .utils import *

def index(request):
    return redirect('/images/load')

def get_img(request, key_url):
    img = get_img_by_key(key_url)
    if img is None:
        return HttpResponseNotFound('INVALID LINK')
    context = {}
    context['img_url'] = img.url
    return TemplateResponse(request, 'img_template.html', context)

def load_image(request):
    return TemplateResponse(request, 'index.html')

def image_api(request):
    x, y = gen_link(request)
    response = {'link': x, 'img_url': y}
    return JsonResponse(data=response)



