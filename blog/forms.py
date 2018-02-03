from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    data = forms.ImageField(label = 'Selec a file')

    class Meta:
        model = Post
        fields = ('title', 'text', 'data')
