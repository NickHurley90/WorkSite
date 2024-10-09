from .models import Employer, StaffRegister
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['business_email', 'business_address', 'business_id']

class StaffRegisterForm(forms.ModelForm):
    class Meta:
        model = StaffRegister
        fields = ['username', 'password', 'email', 'dob', 'trade_category', 'experience', 'staff_id']
        widgets = {
            'password': forms.PasswordInput(),  
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']