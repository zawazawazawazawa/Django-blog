from django import forms
from .models import Post, Comment, ReComment
import cloudinary
from cloudinary.models import CloudinaryField

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'data')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text')

class ReCommentForm(forms.ModelForm):

    class Meta:
        model = ReComment
        fields = ('name', 'text')
