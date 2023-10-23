from django import forms


class TestForm(forms.Form):
  some_text = forms.CharField(label='Text')
  boolean = forms.BooleanField()
  integer = forms.IntegerField(initial=1)
  email = forms.EmailField(min_length=6)
