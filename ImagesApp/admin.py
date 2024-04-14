from django.contrib import admin
from .models import ImageModel,ImageTypeModel,ImageGroupModel,ImagesQuestionsModel

admin.site.register(ImageModel)
admin.site.register(ImageTypeModel)
admin.site.register(ImageGroupModel)
admin.site.register(ImagesQuestionsModel)