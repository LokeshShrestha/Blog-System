from django.shortcuts import render, redirect
from members.models import UserProfile
from .models import BlogPost
from .forms import BlogPostForm
from django.db.models import Count
# Create your views here.

def blog_home(request):
    if not request.user.is_authenticated:
        return redirect("members:login")
    context = {
        "user": request.user,
        "rank": request.user.userprofile.rank,
        "recent_blogs": BlogPost.objects.all().order_by('-created_at'),
        "top_blogs": BlogPost.objects.annotate(view_total=Count('views')).order_by('-view_total')[:6],
    }
    return render(request, "blog_home.html", context)


def post_blog(request):
    if not request.user.is_authenticated:
        return redirect("members:login")
    if request.user.userprofile.rank != 'author':
        return redirect("members:profile")
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect("blog:blog_home")
    else:
        form = BlogPostForm()
    return render(request, "post_blog.html", {"form": form, "user": request.user, "rank": request.user.userprofile.rank})