from django.db import models
from django.contrib.auth.models import User
from blog.models import BlogPost

from django.dispatch import receiver
# Create your models here.
def user_directory_path(instance, filename):
    return f'profile_pics/{instance.user.username}/{filename}'
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    rank = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reader', 'Reader')
    ], default='reader')
    favorite_blogs = models.ManyToManyField(BlogPost, blank=True, related_name='favorited_by')
    def __str__(self):
        return f"{self.user.username}-{self.rank}"