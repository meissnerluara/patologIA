from django.urls import path
from . import views

app_name = 'StudentsApp'

urlpatterns = [
    path('SelectQuestionType', views.ViewSelectQuestionType, name='SelectQuestionTypeView'),
    path('GetQuestionnaireList/', views.ViewGetQuestionnaireList, name='GetQuestionnaireListView'),
    path('GetQuestionList/<str:pk>', views.ViewGetQuestionsList, name='GetQuestionsListView'),
    path('ResultCard/<str:pk>', views.ViewCurrentQuestionnaireResult, name='CurrentQuestionnaireResultView'),
    path('ResultCardDemarcate/<str:pk>', views.ViewCurrentDemarcateQuestionnaireResult, name='CurrentDemarcateQuestionnaireResultView'),
    path('Result/', views.ViewResult, name='ResultView'),

    ]
