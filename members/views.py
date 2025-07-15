from django.shortcuts import render,redirect

from django.contrib.auth import login, logout

from .models import UserProfile

from . import forms
# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        return redirect("members:profile")
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect("members:login")
    else:
        form = forms.RegistrationForm()
    return render(request,"signup.html",{"form":form})

def login_user(request):
    if request.user.is_authenticated:
        return redirect("members:profile")
    if request.method == "POST":
        form = forms.LoginForm(request,data =request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("members:profile")

    else:
        form = forms.LoginForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("members:login")
    return render(request, "logout.html")

def infouser(request):
    if request.method == "POST":
        form = forms.InfoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.InfoForm()
    return(request,"info.html",{"form":form})
def profile(request):
    return render(request, "profile.html", {"user": request.user})
