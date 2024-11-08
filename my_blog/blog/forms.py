# blog/forms.py
from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # Correct model name
        fields = ['title', 'content']  # You can add 'author' if needed in the form
