# Generated by Django 3.2.8 on 2021-12-02 04:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_alter_posts_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 4, 44, 4, 257600, tzinfo=utc)),
        ),
    ]