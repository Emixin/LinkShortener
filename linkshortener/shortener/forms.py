from django import forms
from django.core.exceptions import ValidationError
import re


def validate_url(url):
    regex = r'^https://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$'
    if not re.match(regex, url):
        raise ValidationError("Invalid Link")
    

class LinkForm(forms.Form):
    url = forms.URLField(label='Original URL', validators=[validate_url])