from django import forms
from .models import Image
from . models import Text
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","image")
class TextF(forms.ModelForm):
    class Meta:
        model=Text
        fields=("name","text")
        