from .models import DemarcateQuestion,DemarcateQuestionsModel
from QuestionsApp.models import QuestionsModel, QuestionGroupModel
from ImagesApp.models import ImageModel
from django import forms
from django.db.models import Q


class SelectImageForm(forms.ModelForm):
    Question_Image = forms.ModelChoiceField(required=False, queryset=ImageModel.objects.all(), label="", empty_label="Selecione o número da imagem", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = DemarcateQuestion
        fields = ['Question_Image']
        exclude = ['StartX','StartY','Width','Height','Area','Related_Question']


class CreateDemarcateQuestionsForm(forms.ModelForm):
    Group_Name_Of_Quesitons = forms.ModelChoiceField(queryset = QuestionGroupModel.objects.filter(Q(Is_Demarcate=True) & Q(Online_Status=True)), label="", empty_label="Selecione o Questionário", widget=forms.Select(attrs={'class': 'custom-select'}))
    Question_Text = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'id':'cDesc','name':'tDesc', 'placeholder':'Descrição do assunto do questionário'}))
    Question_Marks = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number','min':'0','value':'1', 'step':'0.5', 'id':'cIdPeso','name':'tIdPeso', 'placeholder':'0.00'}))
    Image_For_Question = forms.ModelChoiceField(required=False, queryset=ImageModel.objects.all(), label="", empty_label="Selecione o número da imagem", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = DemarcateQuestionsModel
        fields = ['Question_Text', 'Question_Marks', 'Group_Name_Of_Quesitons']
        exclude = ['Id_Question','Question_Number', 'Type_Of_Question','Image_For_Question']

class GetQuestionnaireListForm(forms.ModelForm):
    Name_Of_Group = forms.ModelChoiceField(queryset = QuestionGroupModel.objects.filter(Q(Is_Demarcate=True) & Q(Online_Status=True)), label="", empty_label="Selecione o Questionário", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = QuestionGroupModel
        fields = ['Name_Of_Group']
        exclude = ['Is_Right','Option_Text','Option']