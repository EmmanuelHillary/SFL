from django.contrib import admin
from .models import UserProfile, UserFPLCreate, UserFPLPick, Captain

admin.site.register(UserProfile)
admin.site.register(UserFPLCreate)
admin.site.register(UserFPLPick)
admin.site.register(Captain) 
