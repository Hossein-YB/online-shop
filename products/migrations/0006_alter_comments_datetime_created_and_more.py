# Generated by Django 4.1.3 on 2022-12-16 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_comments_datetime_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 5, 38, 43, 265191, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='products',
            name='datetime_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 16, 5, 38, 43, 264275, tzinfo=datetime.timezone.utc)),
        ),
    ]
