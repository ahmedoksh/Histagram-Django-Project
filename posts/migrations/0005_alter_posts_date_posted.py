# Generated by Django 3.2.8 on 2021-11-21 12:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_posts_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 21, 12, 40, 25, 834280, tzinfo=utc)),
        ),
    ]