from django import forms


class LocationForm(forms.Form):
    first_location = forms.CharField(label='First Location Here', widget=forms.TextInput(
        attrs={
            'placeholder': 'First Location Here',
            'class': 'input',
        }
    ))
    second_location = forms.CharField(label='Second Location Here', widget=forms.TextInput(
        attrs={
            'placeholder': 'Second Location Here',
            'class': 'input',
        }
    ))

    def clean_first_location(self):
        first_location = self.cleaned_data.get('first_location')
        return first_location

    def clean_second_location(self):
        second_location = self.cleaned_data.get('second_location')
        return second_location
