from django import forms
from .models import BlogPost,Comment
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','tags','category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter blog title', 'class': 'text'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your blog content here...', 'class': 'text'}),
            'tags': forms.TextInput(attrs={'placeholder': 'Add tags (comma separated)', 'class': 'text'}),
            'category': forms.Select(attrs={'placeholder': 'Select a category', 'class': 'text'}),
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Comment here...', 'class': 'text'}),
        }