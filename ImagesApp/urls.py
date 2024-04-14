from django.urls import path
from . import views

app_name = 'ImagesApp'

urlpatterns = [
    path('CreateImage/', views.ViewCreateImage, name='CreateImageView'),
    path('ImagesGrid/<str:pk>', views.ViewImagesGrid, name='GridImages'),
    path('DeleteImage/<str:pk>', views.ViewDeleteImage, name='DeleteImageView'),
    path('EditImage/<str:pk>', views.ViewEditImage, name='EditImageView'),

]
