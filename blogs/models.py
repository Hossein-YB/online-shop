from django.db import models, transaction
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class BlogCategories(models.Model):
    name = models.CharField(max_length=1000, verbose_name=_("category"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name="categories", verbose_name=_("creator"), )
    count_search = models.PositiveIntegerField(default=1)
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("created datetime"))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("update datetime"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:blog_post_list', args=[self.id, ])

    @classmethod
    def get_top_category(cls):
        categories = cls.objects.all().order_by('-count_search')[:5]
        return categories


class CategorySearchHistory(models.Model):
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE,
                                 related_name="count_history_search", verbose_name=_("category"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name="user_search_category", verbose_name=_("user"))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("created datetime"))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("update datetime"))

    @classmethod
    def insert_category_search(cls, category_id, user):
        with transaction.atomic():
            category = BlogCategories.objects.get(BlogCategories.id == category_id)
            instance = cls.objects.create(category=category, user=user)
            category.count_search += 1
            category.save()
            return instance


class Post(models.Model):
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


class PostCategories(models.Model):
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE,
                                 related_name="post_categories", verbose_name=_("category"))
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="post_categories", verbose_name=_("post"))


