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
