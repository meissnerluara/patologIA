from django.db import models
import uuid


# Create your models here.
class DemarcateQuestion(models.Model):
    Id_Marked = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    StartX = models.IntegerField(blank=True, null=True)
    StartY = models.IntegerField(blank=True, null=True)
    Width = models.IntegerField(blank=True, null=True)
    Height = models.IntegerField(blank=True, null=True)
    Area = models.IntegerField(blank=True, null=True)
    Question_Image = models.ForeignKey('ImagesApp.ImageModel', on_delete = models.CASCADE, verbose_name="Link Image", blank=True, null=True)
    Related_Question = models.ForeignKey('DemarcateQuestionsModel', on_delete = models.CASCADE, verbose_name="Related Question", blank=True, null=True)

    def __str__(self):
        return str(self.Related_Question)

class DemarcateQuestionsModel(models.Model):
    def number():
        no = DemarcateQuestionsModel.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
        
    Id_Question = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Question_Number = models.IntegerField(unique=True, default=number)
    Question_Text = models.CharField(max_length=5000, blank=True, null=True)
    Question_Marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Group_Name_Of_Quesitons = models.ForeignKey('QuestionsApp.QuestionGroupModel', on_delete = models.CASCADE, verbose_name="Group Name of Subject", blank=True, null=True)    
    def __str__(self):
        return self.Question_Text

