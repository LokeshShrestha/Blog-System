from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request, "blog_home.html")