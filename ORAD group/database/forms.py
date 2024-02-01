# forms.py
from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['id', 'fullname','email','phone_number', 'is_active', 'date_joined' ]  # Update fields as per your model
