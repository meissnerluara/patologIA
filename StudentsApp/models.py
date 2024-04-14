from django.db import models
import uuid
from django.utils import timezone
from QuestionsApp.models import QuestionGroupModel


# class StudentPerformance(models.Model):
#     StudentPerformance_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     Student_Information = models.ForeignKey('AccountsApp.CustomUserModel', on_delete=models.DO_NOTHING)
#     Question_Information = models.ForeignKey('QuestionsApp.QuestionsModel', on_delete=models.CASCADE)
#     Question_Group_Information = models.ForeignKey('QuestionsApp.QuestionGroupModel', on_delete=models.DO_NOTHING, default=QuestionGroupModel.objects.first().pk)
#     Score_Per_Question = models.DecimalField(max_digits=10, decimal_places=2)
#     Completed_At = models.DateTimeField(auto_now_add=True)

class StudentPerformance(models.Model):
    StudentPerformance_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Student_Information = models.ForeignKey('AccountsApp.CustomUserModel', on_delete=models.CASCADE)
    Question_Information = models.ForeignKey('QuestionsApp.QuestionsModel', on_delete=models.CASCADE)
    Question_Group_Information = models.ForeignKey('QuestionsApp.QuestionGroupModel', on_delete=models.CASCADE, default=1)
    Score_Per_Question = models.DecimalField(max_digits=10, decimal_places=2)
    Completed_At = models.DateTimeField(auto_now_add=True)

    def get_default_question_group_id():
        default_group = QuestionGroupModel.objects.first()
        if default_group:
            return default_group.pk
        else:
            return 1

    Question_Group_Information.default = get_default_question_group_id

    def __str__(self):
        return str(self.StudentPerformance_ID)

#For Demarcate Quizes

class StudentPerfomranceInDemarcateQuizes(models.Model):
    StudentPerformance_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Student_Information = models.ForeignKey('AccountsApp.CustomUserModel', on_delete=models.CASCADE)
    Question_Information = models.ForeignKey('DemarcateApp.DemarcateQuestionsModel', on_delete=models.CASCADE)
    Question_Group_Information = models.ForeignKey('QuestionsApp.QuestionGroupModel', on_delete=models.CASCADE, default=1)
    Score_Per_Question = models.DecimalField(max_digits=10, decimal_places=2)
    Completed_At = models.DateTimeField(auto_now_add=True)

    def get_default_question_group_id():
        default_group = QuestionGroupModel.objects.filter(Is_Demarcate=True).first()
        if default_group:
            return default_group.pk
        else:
            return 1

    Question_Group_Information.default = get_default_question_group_id

    def __str__(self):
        return str(self.StudentPerformance_ID)