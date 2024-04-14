from QuestionsApp.models import QuestionGroupModel
from django import forms

class GetQuestionnaireListForm(forms.ModelForm):
    Name_Of_Group = forms.ModelChoiceField(
    queryset=QuestionGroupModel.objects.filter(Online_Status=True, Is_Demarcate=False),
    label="",
    empty_label="Selecione o nome do questionário",
    widget=forms.Select(attrs={'class': 'custom-select'})
)
    class Meta:
        model = QuestionGroupModel
        fields = ['Name_Of_Group']
        exclude = ['Is_Right','Option_Text','Option']