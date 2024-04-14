from django.urls import path
from . import views

app_name = 'ResultsApp'

urlpatterns = [
    path('', views.ViewStudentResults, name='StudentsResultsView'),
    path('GetQuestionnaire/', views.ViewGetQuestionnaire, name="GetQuestionnaireView"),
    path('GetDoneQuestionnaire/<str:pk>/', views.ViewGetStudentDoneQuestionnaire, name="GetStudentDoneQuestionnaireView"),
    path('GetDemarcateDoneQuestionnaire/<str:pk>/', views.ViewGetStudentDemarcateDoneQuestionnaire, name="GetStudentDemarcateDoneQuestionnaireView"),
    path('SearchResult/<str:pk>/', views.ViewSearchStudentPerformance, name='SearchStudentPerformanceView'),
]
