# Generated by Django 4.1.3 on 2023-03-18 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_comments_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 56, 0, 48323)),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 16, 56, 0, 47486)),
        ),
    ]
