# Generated by Django 3.2.8 on 2021-11-23 04:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0021_auto_20211122_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default='', upload_to='PostsImages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='userposts', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 4, 32, 47, 800703, tzinfo=utc)),
        ),
    ]
