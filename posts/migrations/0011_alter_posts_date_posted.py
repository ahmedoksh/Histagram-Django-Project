# Generated by Django 3.2.8 on 2021-11-23 04:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_posts_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 4, 14, 27, 524284, tzinfo=utc)),
        ),
    ]
