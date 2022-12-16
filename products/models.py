from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_("product Image"), upload_to='product/product_image/')

    datetime_created = models.DateTimeField(default='django.utils.timezone.now')
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, ])


class Comments(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments', )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments', )
    body = models.TextField(verbose_name=_("comment message"))
    star = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_("whats your score"))
    active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(default='django.utils.timezone.now')
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("product_detail", args=(self.product.id, ))

    def __str__(self):
        return self.body

