from django.shortcuts import render
from . import forms
# Create your views here.
def login_user(request):
    form = forms.LoginForm()
    context = {
        "form":form,
    }
    return render(request, "login.html", context)
def register_user(request):
    form = forms.RegistrationForm()
    context ={
        "form": form,
    }
    return render(request, "signup.html", context)