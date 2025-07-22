from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
import re

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ["username","email","password1","password2"]
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Enhanced email validation
        if not email:
            raise forms.ValidationError("Email is required.")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            raise forms.ValidationError("Please enter a valid email address.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different email or try logging in.")
        return email.lower()
    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        # Enhanced password validation
        if not password:
            raise forms.ValidationError("Password is required.")

        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")

        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Password must contain at least one number.")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

class LoginForm(AuthenticationForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        for field_name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

class InfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio','profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control text'})
        }
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['bio'].widget.attrs['class'] = 'form-control text'
        self.fields['bio'].widget.attrs['placeholder'] = 'Tell us about yourself'
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
        self.fields['profile_picture'].widget.attrs['placeholder'] = 'Upload a profile picture'


