from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Blog(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name="user_posts", verbose_name=_("creator"), )
    title = models.CharField(max_length=1000, verbose_name=_("post title"))
    image = models.ImageField(upload_to="blog/blog_title/", verbose_name=_("post image"))
    body = RichTextField(verbose_name=_("post text"))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("created datetime"))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("update datetime"))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id, ])




