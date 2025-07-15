from django.urls import path,include
from . import views
app_name = "blog"
urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("post/", views.post_blog, name="post_blog"),
]