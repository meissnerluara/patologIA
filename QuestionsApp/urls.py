from django.urls import path
from . import views

app_name = 'QuestionsApp'

urlpatterns = [
    path('SelectQuestionType/', views.ViewSelectQuestionType, name='SelectQuestiontypeView'),
    path('CreateQuestionGroup/', views.ViewCreateQuestionGroup, name='CreateQuestionGroupView'),
    path('CreateQuestionGroup/<str:pk>/', views.ViewEditQuestionGroup, name='EditQuestionGroupView'),
    path('DeleteQuestionGroup/<str:pk>/', views.ViewDeleteQuestionGroup, name='DeleteQuestionGroupView'),
    path('CreateQuestion/', views.ViewCreateQuestion, name='CreateQuestionView'),
    path('ImagesGrid/', views.ViewImagesGrid, name='ImagesGridView'),
    path('EditQuestion/<str:question_number>', views.ViewEditQuestion, name='EditQuestionView'),
    path('DeleteQuestion/<str:question_number>', views.ViewDeleteQuestion, name='DeleteQuestionView'),

    path('CreateOption/', views.ViewCreateOption, name='CreateOptionView'),
    path('EditOption/<str:pk>', views.ViewEditOption, name='EditOptionView'),
    path('DeleteOption/<str:pk>', views.ViewDeleteOption, name='DeleteOptionView'),
]
