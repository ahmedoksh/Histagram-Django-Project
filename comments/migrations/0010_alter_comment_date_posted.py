# Generated by Django 3.2.8 on 2021-11-23 04:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_alter_comment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 4, 15, 22, 702215, tzinfo=utc)),
        ),
    ]
