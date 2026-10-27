from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    # email  = forms.EmailField(max_length=254,help_text='Required')
    
    class Meta:
        model = CustomUser
        fields =('username','email')