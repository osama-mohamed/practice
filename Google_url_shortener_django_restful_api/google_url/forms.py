from django import forms


class UrlForm(forms.Form):
    url = forms.CharField(label='URL', widget=forms.TextInput(
        attrs={
            'placeholder': 'Long URL Here',
            'class': 'input',
        }
    ))

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if '.' not in url:
            raise forms.ValidationError('There is not dot here!')
        if len(url) < 6:
            raise forms.ValidationError('This is not a valid url!')
        return url

