from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('Profile Picture', folder='profile_pic', null=True, blank=True, default="https://res.cloudinary.com/dk9m0i2pg/image/upload/f_auto,q_auto/v1/profile_pic/wsftoet4mz3l9eqeysyi")
    bio = models.TextField(null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username
