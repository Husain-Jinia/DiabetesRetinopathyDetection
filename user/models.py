from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    age = models.IntegerField(max_length=256,  null=True, blank=True)
    profile_picture = models.ImageField(default = 'default.png', upload_to = 'profile_pics', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    