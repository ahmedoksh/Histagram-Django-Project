# Generated by Django 3.2.8 on 2021-11-23 04:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0022_auto_20211122_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 4, 34, 59, 284147, tzinfo=utc)),
        ),
    ]
