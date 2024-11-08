# blog/forms.py
from django import forms
from .models import BlogPost, Comment  # Ensure Comment is imported

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
