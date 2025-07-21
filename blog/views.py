from django.shortcuts import render, redirect
from members.models import UserProfile
from .models import BlogPost
from .forms import BlogPostForm, CommentForm
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
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect("blog:blog_home")
    else:
        form = BlogPostForm()
    return render(request, "post_blog.html", {"form": form, "user": request.user, "rank": request.user.userprofile.rank})

def blog_details(request,id):
    blog = BlogPost.objects.get(id = id)
    comments = blog.comments.all()
    if request.user.is_authenticated:
        blog.views.add(request.user)
    else:
        return redirect("members:login")
    if request.method == "POST":
        #  like
        if "like_this" in request.POST:
            if request.user not in blog.likes.all():
                blog.likes.add(request.user)
            else:
                blog.likes.remove(request.user)
            return redirect("blog:blog_details", id=blog.id)
        
        # Delete comment 
        if "delete_comment" in request.POST:
            comment_id = request.POST.get("delete_comment")
            try:
                a = comments.get(id=comment_id)
                if request.user == a.commentor:
                    a.delete()
            except:
                pass
            return redirect("blog:blog_details", id=blog.id)
        
        #  Put ccomment
        if "add-comment" in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = blog
                comment.commentor = request.user
                comment.save()
                return redirect("blog:blog_details", id=blog.id)
    form = CommentForm()
    context = {
        "blog": blog,
        "comment_form": form,
        "comments": comments,
        "rank": request.user.userprofile.rank,
    }
    return render(request,"blog_details.html",context)

def edit_blog(request,id):
    blog = BlogPost.objects.get(id = id)
    if not request.user.is_authenticated:
        return redirect("members:login")
    
    if request.user != blog.author:
        return redirect("blog:blog_details", id=blog.id)
    
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect("blog:blog_details", id=blog.id)
    else:
        form = BlogPostForm(instance=blog)
    context = {
        "blog": blog,
        "form": form,
        "rank": request.user.userprofile.rank,
    }
    return render(request,"edit_blog.html",context)
def delete_blog(request, id):
    blog = BlogPost.objects.get(id=id)
    if not request.user.is_authenticated:
        return redirect("members:login")
    
    if request.user != blog.author:
        return redirect("blog:blog_details", id=blog.id)
    
    if request.method == "POST":
        blog.delete()
        return redirect("blog:blog_home")
    
    context = {
        "blog": blog,
        "rank": request.user.userprofile.rank,
    }
    return render(request, "delete_blog.html", context)

from django.db.models import Q

def search_blogs(request):
    query = request.GET.get('q')
    # print(f"Search query: {query}")
    if query:
        result = BlogPost.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(author__username__icontains=query)
        ).distinct()
    else:
        result = BlogPost.objects.none()
    # print(f"Search results: {result}")
    context = {
        "result": result,
        "query": query,
        "rank": request.user.userprofile.rank,
    }
    return render(request, "search.html", context)
