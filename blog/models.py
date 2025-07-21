from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
def user_directory_path(instance, filename):
    return f'blog_images/{instance.author.username}/{filename}'
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('technology', 'Technology'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        ('entertainment', 'Entertainment'),
        ('education', 'Education'),
        ('business', 'Business'),
        ('lifestyle', 'Lifestyle'),
        ('news', 'News'),
        ('gaming', 'Gaming'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    content = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.ManyToManyField(User, related_name='views', blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True,  choices= CATEGORY_CHOICES)
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    @property
    def like_count(self):
        return self.likes.count()
    @property
    def view_count(self):
        return self.views.count()
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
    def __str__(self):
        return f"Comment by {self.commentor} on {self.post}"