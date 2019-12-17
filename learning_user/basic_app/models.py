from django.db import models
from django.contrib.auth.models import User

class userprofileinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_url = models.URLField( blank = True)
    profile_pic = models.ImageField( upload_to = 'profile_pics' , blank = True )
    def __str__(self):
        return self.user.username

class article(models.Model):
    name = models.CharField(max_length = 40)
    content = models.CharField(max_length = 40)
    def __str__(self):
        return self.name
