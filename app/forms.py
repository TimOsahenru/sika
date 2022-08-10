from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import House, User


class MyCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class HouseForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['rented', 'agent']


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'phone', 'email', 'bio']
