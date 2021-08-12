from django.contrib import admin
from django.conf import settings
from .models import UserProfile,BrokerCategory,BrokerSubCategory,Agency

# Register your models here.
admin.site.register(Agency)
admin.site.register(BrokerCategory)
admin.site.register(BrokerSubCategory)
# here can add user 
admin.site.register(UserProfile)
