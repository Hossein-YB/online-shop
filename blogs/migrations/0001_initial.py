# Generated by Django 4.1.3 on 2023-01-09 18:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='post title')),
                ('image', models.ImageField(upload_to='blog/blog_title/', verbose_name='post image')),
                ('body', ckeditor.fields.RichTextField(verbose_name='post text')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='created datetime')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='update datetime')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
        ),
    ]