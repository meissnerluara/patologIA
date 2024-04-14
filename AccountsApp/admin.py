from django.contrib import admin
from .models import RoleModel,CustomUserModel

admin.site.register(RoleModel)
admin.site.register(CustomUserModel)
