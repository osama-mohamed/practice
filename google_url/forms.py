from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='URL', widget=forms.TextInput(
        attrs={
            'placeholder': 'Long URL Here',
            'class': 'input',
        }
    ))
