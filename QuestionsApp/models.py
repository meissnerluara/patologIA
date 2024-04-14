from django.db import models
import uuid
import math

# Questão de Demarcação ou Múltipla Escolha!
class QuestionTypesModel(models.Model):
    Id_Type_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Category = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.Category

class QuestionsModel(models.Model):
    def number():
        no = QuestionsModel.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
        
    Id_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Question_Number = models.IntegerField(unique=True, default=number)
    Question_Text = models.CharField(max_length=5000, blank=True, null=True)
    Question_Marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Type_Of_Question = models.ForeignKey('QuestionTypesModel', on_delete = models.CASCADE, verbose_name="Type of Question", blank=True, null=True)
    Group_Name_Of_Quesitons = models.ForeignKey('QuestionGroupModel', on_delete = models.CASCADE, verbose_name="Group Name of Subject", blank=True, null=True)
    Video_For_Question = models.ForeignKey('VideosApp.VideoModel', on_delete = models.CASCADE, verbose_name="Link Video", blank=True, null=True)
    Image_For_Question = models.ForeignKey('ImagesApp.ImageModel', on_delete = models.CASCADE, verbose_name="Link Image", blank=True, null=True)
    
    def __str__(self):
        return self.Question_Text


class QuestionGroupModel(models.Model):
    def number():
        no = QuestionGroupModel.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
        
    Id_QuestionGroup = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Group_Number = models.IntegerField(unique=True, default=number)
    Name_Of_Group = models.CharField(max_length=150, blank=True, null=True)
    Subject_Description = models.CharField(max_length=250, blank=True, null=True)
    Date_Of_Creation = models.DateField(blank=True, null=True)
    Is_Demarcate = models.BooleanField(default = False ,blank=True, null=True)
    Online_Status = models.BooleanField(default = False,blank=True, null=True)
    Creators_Information = models.ForeignKey('AccountsApp.CustomUserModel', models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.Name_Of_Group

class MCQModel(models.Model):
    Id_MCQs = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Option = models.CharField(max_length=1, blank=True, null=True)
    Option_Text = models.CharField(max_length=1000, blank=True, null=True)
    Is_Right = models.BooleanField(default=False)
    Related_Question = models.ForeignKey('QuestionsModel', on_delete = models.CASCADE, verbose_name="Related Question")

    def __str__(self):
        return self.Option_Text