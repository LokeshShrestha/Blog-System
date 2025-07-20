from django import forms
from .models import BlogPost,Comment
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','tags','category']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter blog title'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Write your blog content here...'})
        self.fields['tags'].widget.attrs.update({'placeholder': 'Add tags (comma separated)'})
        self.fields['category'].widget.attrs.update({'placeholder': 'Select a category'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Comment here...', 'class': 'text'}),
        }