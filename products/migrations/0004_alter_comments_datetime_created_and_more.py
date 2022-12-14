# Generated by Django 4.1.3 on 2022-12-13 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_image_alter_comments_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 16, 26, 2, 935770, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 13, 16, 26, 2, 934987, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='product/product_image/', verbose_name='product Image'),
        ),
    ]
