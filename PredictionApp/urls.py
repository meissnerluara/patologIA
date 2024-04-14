from django.urls import path
from . import views

app_name = 'PredictionApp'

urlpatterns = [
    path('', views.ViewPredictTuberclousis, name='PredictTuberclousisView'),
    # path('COVID/', views.ViewPredictCOVID, name='PredictCOVIDView'),
]
