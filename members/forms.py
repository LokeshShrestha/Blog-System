from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
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
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['placeholder'] = 'Tell us about yourself'
        self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
        self.fields['profile_picture'].widget.attrs['placeholder'] = 'Upload a profile picture'


