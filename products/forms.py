from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]


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
