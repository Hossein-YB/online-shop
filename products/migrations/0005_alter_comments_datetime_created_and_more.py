# Generated by Django 4.1.3 on 2022-12-15 15:45

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comments_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 15, 45, 14, 126309, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 15, 45, 14, 125550, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
