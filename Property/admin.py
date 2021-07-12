from django.contrib import admin
from django.conf import settings
from .models import Agency,Broker
from Property.models import BrokerCategory

# Register your models here.
admin.site.register(Agency)

# here can add user 
admin.site.register(Broker)
admin.site.register(BrokerCategory)
