from django import forms
from .models import Tales

class TalesForm(forms.ModelForm):
    class Meta:
        model = Tales
        fields = [
          'title',
          'author',
          'genre',
          'content', 
        ]

class RawTaleForm(forms.Form):
    title = forms.CharField()
    Author = forms.CharField()
    Genre = forms.CharField()
    Content = forms.CharField(max_length=3000, widget=forms.Textarea)
