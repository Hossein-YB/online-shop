# Generated by Django 4.1.3 on 2023-03-18 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_comments_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 19, 20, 38, 895370)),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 19, 20, 38, 894167)),
        ),
    ]
