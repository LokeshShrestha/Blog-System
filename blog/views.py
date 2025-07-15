from django.shortcuts import render, redirect
from members.models import UserProfile
from .forms import BlogPostForm
# Create your views here.

def data(request):
    if not request.user.is_authenticated:
        return redirect("members:login")
    # Get the user's profile
    user_profile = UserProfile.objects.get(user=request.user)
    return user_profile
def blog_home(request):
    if not request.user.is_authenticated:
        return redirect("members:login")
    return render(request, "blog_home.html",{"user": request.user, "rank": data(request).rank})


def post_blog(request):
    if not request.user.is_authenticated:
        return redirect("members:login")
    if request.user.userprofile.rank != 'author':
        return redirect("members:profile")
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user.userprofile
            blog_post.save()
            return redirect("blog:blog_home")
    else:
        form = BlogPostForm()
    return render(request, "post_blog.html", {"form": form})