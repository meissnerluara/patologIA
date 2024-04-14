from django.contrib import admin
from .models import QuestionTypesModel,QuestionsModel,QuestionGroupModel,MCQModel

admin.site.register(QuestionTypesModel)
admin.site.register(QuestionsModel)
admin.site.register(QuestionGroupModel)
admin.site.register(MCQModel)