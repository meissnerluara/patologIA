from django.urls import path
from . import views

app_name = 'CasesApp'

urlpatterns = [
    path('', views.ViewUploadFile, name='ViewUploadFileView'),
]
