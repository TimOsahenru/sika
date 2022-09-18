from .models import House, Agent
from django import forms


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['agent']


class HouseCreate(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['agent', 'available']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['username', 'avatar', 'email', 'phone_no', 'about_me']

