# Generated by Django 3.2.8 on 2021-11-22 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='DefaultPP.jpg', upload_to='ProfilePictures'),
        ),
    ]