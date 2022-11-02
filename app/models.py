from django.db import models
from django.contrib.auth.models import AbstractUser


class Agent(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.IntegerField(null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    avatar = models.ImageField(default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class HouseType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class House(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    no_of_rooms = models.IntegerField()
    # no_of_bathrooms = models.IntegerField()
    # garage = models.BooleanField()
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    type_of_house = models.ForeignKey(HouseType, on_delete=models.SET_NULL, null=True, blank=True)
    rent_price = models.IntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent.username

    @property
    def image_one_url(self):
        try:
            url = self.image_one.url
        except:
            url = ''
        return url

    def image_two_url(self):
        try:
            url = self.image_two.url
        except:
            url = ''
        return url

    def image_three_url(self):
        try:
            url = self.image_three.url
        except:
            url = ''
        return url


    class Meta:
        ordering = ['-created_at']
