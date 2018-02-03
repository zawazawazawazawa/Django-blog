from django import forms
from .models import Post
import cloudinary
from cloudinary.models import CloudinaryField

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'data')
