# Generated by Django 3.2.8 on 2021-12-02 03:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0025_alter_comment_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 3, 44, 55, 761845, tzinfo=utc)),
        ),
    ]
