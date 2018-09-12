from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['likes']
