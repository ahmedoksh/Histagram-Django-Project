# Generated by Django 3.2.8 on 2021-11-21 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211121_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 21, 11, 38, 15, 749872, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]