# forms.py

from django import forms

class StudentSearchForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
