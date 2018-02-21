from django import forms


class UserForm(forms.Form):
    user_name_one = forms.CharField(label='First User', widget=forms.TextInput(
        attrs={
            'placeholder': 'GitHub First User Here',
            'class': 'input',
        }
    ))
    user_name_two = forms.CharField(label='Second User', widget=forms.TextInput(
        attrs={
            'placeholder': 'GitHub Second User Here',
            'class': 'input',
        }
    ))
