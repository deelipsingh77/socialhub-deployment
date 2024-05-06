from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('Profile Picture', folder='profile_pic', null=True, blank=True, default='https://pixabay.com/get/g4d9249f2719549e599655433fde32c4a91e0dbdf75b1907ab5623fc542afeaba66bc2bf5f30a86738adcf50ccc41dbdf.svg')
    bio = models.TextField(null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username
