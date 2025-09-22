from django.db import models
from django.contrb.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name = "profile")
    name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 15, blank = True,null = True)

    def __str__(self):
        return self.name or self.user.username

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    address = models.CharField(max_length = 150)

    def __str__(self):
        return self.name