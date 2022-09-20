from .models import House, Agent
from django import forms


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['agent']
        widgets = {
            'type_of_house': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'rent_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_one': forms.FileInput(attrs={'class': 'form-control'}),
            'image_two': forms.FileInput(attrs={'class': 'form-control'}),
            'image_three': forms.FileInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class HouseCreate(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['agent', 'available']
        widgets = {
            'type_of_house': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'rent_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_one': forms.FileInput(attrs={'class': 'form-control'}),
            'image_two': forms.FileInput(attrs={'class': 'form-control'}),
            'image_three': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['username', 'avatar', 'email', 'phone_no', 'about_me']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control'})
        }

