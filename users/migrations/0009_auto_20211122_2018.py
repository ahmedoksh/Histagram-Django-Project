# Generated by Django 3.2.8 on 2021-11-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='ahmed', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(default='ahmed', max_length=300),
        ),
    ]
