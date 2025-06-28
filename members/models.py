from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('writer', 'Writer'),
        ('reader', 'Reader'),
    ])