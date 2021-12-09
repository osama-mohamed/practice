from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = [
      'title',
      'content',
    ]
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields:
      new_data = {
        'placeholder':f'Article {str(field).title()}',
        'class': 'form-control',
      }
      self.fields[str(field)].widget.attrs.update(new_data)
      self.fields[str(field)].label = f'Article {str(field).title()}'
    self.fields['content'].widget.attrs.update({'rows': 4})

  def clean(self):
    data = self.cleaned_data
    title = data.get('title')
    qs = Article.objects.filter(title__icontains=title)
    if qs.exists():
      self.add_error('title', f'\"{title}\" is already in use. Please pick another title.')
    return data
  
  
class ArticleUpdateForm(ArticleForm):
  def clean(self):
    return super(ArticleForm, self).clean()