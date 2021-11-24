from django import forms
from django.core.exceptions import ValidationError

class ArticleForm(forms.Form):
  title = forms.CharField()
  content = forms.CharField()

  # def clean_title(self):
  #   cleaned_data = self.cleaned_data
  #   title = cleaned_data.get('title')
  #   if title.lower().strip() == 'o':
  #     raise forms.ValidationError('This title is taken.')
  #   return title
  
  def clean(self):
    cleaned_data = self.cleaned_data
    title = cleaned_data.get('title')
    content = cleaned_data.get('content')
    if title.lower().strip() == 'os':
      self.add_error('title', 'This title is taken too.')
      # raise forms.ValidationError('This title is taken too.')
    if 'osama' in title.lower() or 'osama' in content.lower() :
      self.add_error('title', 'title osama is not allowed to be here.')
      self.add_error('content', 'content osama is not allowed to be here.')
      raise ValidationError('osama is not allowed')      
    return cleaned_data