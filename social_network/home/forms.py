from django import forms
from .models import Post


class HomeForm(forms.ModelForm):
    # (required=False) to make it optional not required
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a Post ...',
            'style': 'max-width: 80%;'
        }
    ))

    class Meta:
        model = Post
        fields = ['post',]
