from django import forms
from .models import Link


class LinkForm(forms.Form):
    url = forms.URLField(label='Original URL')
    shortened_url = forms.CharField(label='Your Shortened URl', required=False)

    def clean_shortened_url(self):
        shortened = self.cleaned_data.get('shortened_url')
        if shortened and len(shortened) < 6:
            raise forms.ValidationError("Shortened URL length should be at least 6")
        return shortened