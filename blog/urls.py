from django.urls import path,include
from . import views
app_name = "blog"
urlpatterns = [
    path("", views.blog_home, name="blog_home"),
    path("post/", views.post_blog, name="post_blog"),
    path("<int:id>/",views.blog_details,name = "blog_details"),
    path("edit/<int:id>/",views.edit_blog,name = "edit_blog"),
    path("delete/<int:id>/", views.delete_blog, name="delete_blog"),
    path("search/", views.search_blogs, name="search_blogs"),
]