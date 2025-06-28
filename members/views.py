from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def login_user(request):
    form = forms.LoginForm()
    context = {
        "form":form,
    }
    return render(request, "login.html", context)
def register_user(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save
            return redirect("login")
    else:
        form = forms.RegistrationForm()
    context ={
        "form": form,
    }
    return render(request, "signup.html", context)