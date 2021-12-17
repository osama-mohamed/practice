from django import forms

from .models import Recipe, RecipeIngredient, RecipeIngredientImage

class RecipeForm(forms.ModelForm):
  error_css_class = 'error-field'
  required_css_class = 'required-field'
  name = forms.CharField(help_text='This is your help! <a href="/contact/">Contact us</a>')
  # name = forms.CharField(
  #   widget=forms.TextInput(
  #     attrs={
  #       'class': 'form-control',
  #       'placeholder': 'Recipe name'
  #     }
  #   )
  # )
  # description = forms.CharField(
  #   label='Recipe Description',
  #   widget=forms.Textarea(
  #     attrs={
  #       'placeholder': 'Recipe description',
  #       'rows': 6,
  #       'cols': 50
  #     }
  #   )
  # )
  class Meta:
    model = Recipe
    fields = ['name', 'description', 'directions']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # self.fields['name'].label = 'Recipe Name'
    # self.fields['name'].widget.attrs.update({'class': 'form-control-2'})
    self.fields['description'].widget.attrs.update({'rows': 2})
    self.fields['directions'].widget.attrs.update({'rows': 4})
    for field in self.fields:
      # self.fields[str(field)].widget.attrs.update(placeholder=f'Recipe {str(field).title()}')
      new_data = {
        'placeholder':f'Recipe {str(field).title()}',
        'class': 'form-control',
        # 'hx-post': '.',
        # 'hx-trigger': 'keyup changed delay:500ms',
        # 'hx-target': '#recipe-container',
        # 'hx-swap': 'outerHTML'
      }
      self.fields[str(field)].widget.attrs.update(new_data)
      self.fields[str(field)].label = f'Recipe {str(field).title()}'


class RecipeIngredientForm(forms.ModelForm):
  class Meta:
    model = RecipeIngredient
    fields = ['name', 'quantity', 'unit']


class RecipeIngredientImageForm(forms.ModelForm):
  class Meta:
    model = RecipeIngredientImage
    fields = ['image']
    labels = {
      "image": "Extract via Image Upload"
    }