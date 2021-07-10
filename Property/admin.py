from django.contrib import admin
from django.conf import settings

from .models import Agency,Broker
# Register your models here.

admin.site.register(Agency)

# here can add user 
admin.site.register(Broker)