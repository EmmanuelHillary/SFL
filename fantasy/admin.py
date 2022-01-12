from django.contrib import admin
from .models import UserProfile, UserFPLCreate, UserFPLPick, Captain, Cap

admin.site.register(UserProfile)
admin.site.register(UserFPLCreate)
admin.site.register(UserFPLPick)
admin.site.register(Captain) 
admin.site.register(Cap)