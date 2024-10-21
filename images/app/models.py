from django.db import models
from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField()


class Images(models.Model):
    
    img = models.ImageField(
        verbose_name='Image',
        upload_to='images',
    )
    
    key = models.CharField(
        verbose_name='key',
        max_length=6,
        unique=True
    )
    
    def __str__(self):
        return self.img.name
    
    class Meta:
        verbose_name='Image'
        verbose_name_plural='Images'
