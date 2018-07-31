from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'product title',
            }
        )
    )
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'new-class other-class',
                'id': 'my-custom-id',
                'placeholder': 'product description',
                'rows': 12,
                'cols': 25
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
    def clean_title(self, *args, **keargs):
        title = self.cleaned_data.get('title')
        if not 'osama' in title:
            raise forms.ValidationError('This is not a valid title')
        return title
    
    def clean_email(self, *args, **keargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not a valid email')
        return email
        



class RawProductForm(forms.Form):
    title = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'product title',
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'new-class other-class',
                'id': 'my-custom-id',
                'placeholder': 'product description',
                'rows': 12,
                'cols': 25
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
