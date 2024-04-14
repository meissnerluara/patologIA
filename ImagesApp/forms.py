from .models import ImageModel, ImageTypeModel, ImageGroupModel
from django import forms

class CreateImageForm(forms.ModelForm):
    Upload_Image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input', 'id': 'imagem', 'accept': 'image/bmp, image/jpeg, image/png, image/tiff', 'draggable': 'false', 'aria-describedby': 'inputFileAddon', 'onchange': 'previewImage()'}))
    Type_Of_Image = forms.ModelChoiceField(queryset=ImageTypeModel.objects.all(),
        label="",
        empty_label="Tipo de Imagem",
        widget=forms.Select(attrs={'class': 'custom-select'}))
    Image_Group = forms.ModelChoiceField(queryset=ImageGroupModel.objects.all(),
        label="",
        empty_label="Selecione a especialidade da imagem",
        widget=forms.Select(attrs={'class': 'custom-select'}))
    
    class Meta:
        model = ImageModel
        fields = ['Upload_Image','Type_Of_Image','Image_Group']

class DeleteImageForm(forms.ModelForm):
    Image_Group = forms.ModelChoiceField(queryset=ImageGroupModel.objects.all(),
        label="",
        empty_label="Selecione a especialidade da imagem",
        widget=forms.Select(attrs={'class': 'custom-select'}))
    
    class Meta:
        model = ImageModel
        fields = ['Image_Group']
        exclude = ['Upload_Image','Type_Of_Image']