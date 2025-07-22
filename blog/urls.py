from django.urls import path,include
from . import views
app_name = "blog"
urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("blog/post/", views.post_blog, name="post_blog"),
    path("blog/<int:id>/",views.blog_details,name = "blog_details"),
    path("blog/edit/<int:id>/",views.edit_blog,name = "edit_blog"),
    path("blog/delete/<int:id>/", views.delete_blog, name="delete_blog"),
    path("blog/search/", views.search_blogs, name="search_blogs"),
]