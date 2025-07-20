from django.contrib import admin
from .models import BlogPost,Comment
# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','content', 'author', 'created_at']
    search_fields = ['title', 'author']
    list_filter = ['created_at']
    ordering = ['-created_at']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'commentor', 'comment', 'created_at']
    search_fields = ['content', 'commentor']
    list_filter = ['created_at']
    ordering = ['-created_at']