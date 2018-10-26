from django import forms

from .models import Posts, Likes


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('photo', 'description')
