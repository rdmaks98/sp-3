from django.contrib import admin
from django.conf import settings
from .models import Agency,Broker,BrokerCategory,BrokerSubCategory

# Register your models here.
admin.site.register(Agency)
admin.site.register(BrokerCategory)
admin.site.register(BrokerSubCategory)
# here can add user 
admin.site.register(Broker)