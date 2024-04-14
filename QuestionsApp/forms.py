from .models import QuestionTypesModel,QuestionGroupModel,QuestionsModel,MCQModel
from VideosApp.models import VideoModel
from ImagesApp.models import ImageModel
from django import forms
from django.db.models import Q

class SelectQuestionTypeForm(forms.ModelForm):
    Category = forms.ModelChoiceField(required=True, queryset=QuestionTypesModel.objects.all(),label="", empty_label="Selecione o tipo de Questionário", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = QuestionTypesModel
        fields = ['Category']

class CreateQuestionGroupForm(forms.ModelForm):
    
    Name_Of_Group = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'cTitQuiz','name':'tTitQuiz', 'placeholder':'Título do questionário'}))
    Subject_Description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id':'cAssQuiz','name':'tAssQuiz', 'placeholder':'Descrição do assunto do questionário'}))
    class Meta:
        model = QuestionGroupModel
        fields = ['Name_Of_Group','Subject_Description','Date_Of_Creation']
        exclude = ['Group_Number','Creators_Information','Is_Demarcate','Online_Status']
        widgets = {
            'Date_Of_Creation': forms.DateInput(format=('%Y-%m-%d'),
                                                attrs={'class': 'form-control', 
               'id':'cIdDataQuiz',
               'name':'tIdDataQuiz',
               'placeholder':'Data do cadastro do Questionário',
               'type': 'date'
              }),}

class CreateQuestionsForm(forms.ModelForm):
    Group_Name_Of_Quesitons = forms.ModelChoiceField(queryset = QuestionGroupModel.objects.filter(Q(Is_Demarcate=False) & Q(Online_Status=True)),label="", empty_label="Selecione o Questionário", widget=forms.Select(attrs={'class': 'custom-select'}))
    Question_Text = forms.CharField(max_length=5000, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'id':'cDesc','name':'tDesc', 'placeholder':'Descrição do assunto do questionário'}))
    Question_Marks = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'type':'number','min':'0','value':'1', 'step':'0.5', 'id':'cIdPeso','name':'tIdPeso', 'placeholder':'0.00'}))
    Image_For_Question = forms.ModelChoiceField(required=False, queryset=ImageModel.objects.all(), label="", empty_label="Selecione o número da imagem", widget=forms.Select(attrs={'class': 'custom-select'}))
    Video_For_Question = forms.ModelChoiceField(required=False,queryset=VideoModel.objects.all(), label="", empty_label="Selecione o número do vídeo", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = QuestionsModel
        fields = ['Question_Text', 'Question_Marks', 'Group_Name_Of_Quesitons','Image_For_Question','Video_For_Question']
        exclude = ['Id_Question','Question_Number', 'Type_Of_Question']

class EditQuestionsForm(forms.ModelForm):
    Question_Number = forms.ModelChoiceField(queryset=QuestionsModel.objects.values_list('Question_Number', flat=True).distinct().order_by('Question_Number'),label="", empty_label="Selecione o número da pergunta", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = QuestionsModel
        fields = ['Question_Number']
        exclude = ['Id_Question','Question_Marks','Group_Name_Of_Quesitons','Image_For_Question','Video_For_Question','Question_Number', 'Type_Of_Question']

class CreateOptionForm(forms.ModelForm):
    Related_Question = forms.ModelChoiceField(queryset=QuestionsModel.objects.all(),label="", empty_label="Selecione a Descrição da Pergunta", widget=forms.Select(attrs={'class': 'custom-select'}))
    Option_Text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control', 'rows':'5', 'id':'cAssQuiz','name':'tAssQuiz', 'placeholder':'Descrição  da alternativa'}))
    Option = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'class': 'form-control', 'type':'text','id':'cOpcao','name':'tOpcao', 'placeholder':'Opção'}))
    class Meta:
        model = MCQModel
        fields = ['Related_Question','Option_Text','Option']
        exclude = ['Is_Right']

class EditOptionForm(forms.ModelForm):
    Related_Question = forms.ModelChoiceField(queryset=QuestionsModel.objects.all(),label="", empty_label="Selecione o número da pergunta", widget=forms.Select(attrs={'class': 'custom-select'}))
    class Meta:
        model = MCQModel
        fields = ['Related_Question','Is_Right']
        exclude = ['Option_Text','Option']

