from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .validators import validate_url, validate_domain


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='URL',
                          validators=[validate_url, validate_domain],
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Original URL Here'
                              }
                          ))

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     if 'http' in url:
    #         return url
    #     return 'http://' + url

    # # validate data from form
    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     # print(cleaned_data)
    #     url = cleaned_data.get('url')
    #     # print(url)
    #     # url = cleaned_data['url']
    #     # print(url)
    #     # url_validator = URLValidator()
    #     # try:
    #     #     url_validator(url)
    #     # except:
    #     #     raise forms.ValidationError('invalid Url syntax')
    #     # return url
    #
    #
    # # # validate data from field directly
    # # def clean_url(self):
    # #     url = self.cleaned_data['url']
    # #     # print(url)
    # #     url_validator = URLValidator()
    # #     try:
    # #         url_validator(url)
    # #     except:
    # #         raise forms.ValidationError('invalid Url syntax')
    # #     return url
