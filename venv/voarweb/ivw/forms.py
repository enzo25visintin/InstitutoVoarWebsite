from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta: #class used to change behavior of model fields
        model = User
        fields = ['name', 'email', 'password', 'telephone_number', 'company', 'status']
