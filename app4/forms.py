# app4/forms.py

from django import forms

class WordForm(forms.Form):
    word = forms.CharField(label='Enter a word', min_length=3, max_length=5)