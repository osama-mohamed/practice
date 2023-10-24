from django import forms


from .models import Post



class PostModelForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = [
      'user', 
      'title', 
      'slug', 
      'image',
    ]
    exclude = [
      'slug',
    ]
    labels = {
      'title': 'Post Title',
      'image': 'Post Image',
    }















SOME_CHOICES = [
  ('db-value', 'Display Value'),
  ('db-value2', 'Display Value 2'),
  ('db-value3', 'Display Value 3'),
]

INT_CHOICES = [tuple([x, x]) for x in range(0, 101)]
YEARS = [x for x in range(1980, 2031)]

class TestForm(forms.Form):
  date_field = forms.DateField(label='Date', initial="2020-10-01", widget=forms.SelectDateWidget(years=YEARS))
  some_text = forms.CharField(label='Text', initial='Some New Text', widget=forms.Textarea(attrs={'rows': 6, 'cols': 25}))
  choices = forms.CharField(label='Choices', widget=forms.CheckboxSelectMultiple(choices=SOME_CHOICES))
  choices_two = forms.CharField(label='Choices Two', widget=forms.SelectMultiple(choices=SOME_CHOICES))
  boolean = forms.BooleanField()
  integer = forms.IntegerField(initial=1, widget=forms.Select(choices=INT_CHOICES))
  email = forms.EmailField(min_length=6, initial='Your e-mail')


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
