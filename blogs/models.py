from django.db import models, transaction
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class IsActivePostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).select_related("user", 'category')

    def active_posts(self, *args, **kwargs):
        return self.get_queryset(*args, **kwargs).filter(is_active=True)


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

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class CategorySearchHistory(models.Model):
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE,
                                 related_name="count_history_search", verbose_name=_("category"))
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name="user_search_category", null=True, verbose_name=_("user"))
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

    class Meta:
        verbose_name = _("CategorySearchHistory")
        verbose_name_plural = _("CategorySearchHistories")


class Post(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name="user_posts", verbose_name=_("creator"), )
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE,
                                 related_name="category", verbose_name=_("category"), )

    title = models.CharField(max_length=1000, verbose_name=_("post title"))
    image = models.ImageField(upload_to="blog/blog_title/", verbose_name=_("post image"))
    description = models.CharField(max_length=1000, default="this is a test for description",
                                   verbose_name=_("description about this post"))
    like = models.PositiveIntegerField(verbose_name=_("number of like"))
    dis_like = models.PositiveIntegerField(verbose_name=_("number of unlike"))
    body = RichTextField(verbose_name=_("post text"))
    is_active = models.BooleanField(default=True)

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_("created datetime"))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_("update datetime"))

    default_manage = models.Manager()
    objects = IsActivePostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id, ])

    @classmethod
    def search_post_with_word(cls, word):
        posts = cls.objects.all().filter(title__icontains=word)
        return posts

    @classmethod
    def get_posts(cls, numbers=None):
        posts = cls.objects.active_posts().order_by('-datetime_created')[:numbers]
        return posts

    @classmethod
    def get_top_post(cls, numbers=None) -> tuple:
        posts = cls.objects.active_posts().order_by('-like')[:numbers]

        return posts

    @classmethod
    def get_post_detail(cls, post_id):
        posts = cls.objects.active_posts().get(id)
        return posts

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
