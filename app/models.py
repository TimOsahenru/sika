from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class HouseImage(models.Model):
    pass
    # caption =
    # image =
    # user =


class Area(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class HouseType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Change user to agent
class House(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    house_type = models.ForeignKey(HouseType, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(null=True, default='property-2.jpg')
    description = models.TextField(null=True, blank=True)
    nos_of_bedrooms = models.IntegerField(blank=True, null=True)
    nos_of_bathrooms = models.IntegerField(blank=True, null=True)
    rented = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.name

    class Meta:
        ordering = ['-created_at']
