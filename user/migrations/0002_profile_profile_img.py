# Generated by Django 3.2.4 on 2021-06-30 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to='user/'),
        ),
    ]
