from django import forms


class TestForm(forms.Form):
  some_text = forms.CharField(label='Text')
  boolean = forms.BooleanField()
  integer = forms.IntegerField(initial=1)
  email = forms.EmailField(min_length=6)

  def __init__(self, *args, **kwargs):
    super(TestForm, self).__init__(*args, **kwargs)
    self.fields['some_text'].initial = 'Some New Text'
    self.fields['email'].initial = 'Your e-mail'

  def clean_some_text(self, *args, **kwargs):
    some_text = self.cleaned_data.get('some_text')
    if len(some_text) < 10:
      raise forms.ValidationError('The text is too short')
    return some_text
  
  def clean_integer(self, *args, **kwargs):
    integer = self.cleaned_data.get('integer')
    if integer < 10:
      raise forms.ValidationError('The number is too small')
    return integer
