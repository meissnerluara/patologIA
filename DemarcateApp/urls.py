from django.urls import path
from . import views

app_name = 'DemarcateApp'

urlpatterns = [
    path('CreateQuestion/', views.ViewCreateDemarcateQuestion, name='CreateDemarcateQuestionView'),
    path('SelectImage/', views.ViewSelectImage, name='SelectImageView'),
    path('CreateDemarcateArea/<str:pk>', views.ViewCreateDemarcateArea, name='CreateDemarcateAreaView'),
    path('SelectGroupName/', views.ViewGetDemarcateQuestionnaireList, name='GetDemarcateQuestionnaireListView'),
    path('AnswerQuestion/<str:pk>', views.ViewAnswerDemarcateQuestion, name='AnswerDemarcateQuestionView'),
    path('Result/', views.ViewResult, name='ResultView'),

]
