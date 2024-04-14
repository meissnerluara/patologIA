from django import forms
from .models import CasesModel


class CasesForm(forms.ModelForm):
    CaseStudyNumber = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    CaseStudyFileName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    CaseStudyFile = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'id': 'browseFile', 'accept': 'application/pdf', 'draggable': 'false', 'aria-describedby': 'inputFileAddon', 'onchange': 'previewPdf8()'}))
    class Meta:
        model = CasesModel
        fields = ['CaseStudyNumber','CaseStudyFileName','CaseStudyFile']