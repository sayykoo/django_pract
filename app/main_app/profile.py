from django.db import models
from django.contrib.auth.models import User

class Gender(models.TextChoices):
    MEN = "Мужской"
    WOMEN = "Женский"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(choices=Gender, blank=True, max_length=20)
    
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    house = models.CharField(max_length=50, blank=True)
    appartment_num = models.CharField(max_length=50, blank=True)
    image_profile = models.ImageField(null=True, blank=True, upload_to='images/user_profile/')