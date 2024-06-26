# Generated by Django 5.0.4 on 2024-05-21 13:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://pixabay.com/get/g4d9249f2719549e599655433fde32c4a91e0dbdf75b1907ab5623fc542afeaba66bc2bf5f30a86738adcf50ccc41dbdf.svg', max_length=255, null=True, verbose_name='Profile Picture'),
        ),
    ]
