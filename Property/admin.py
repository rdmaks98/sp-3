from django.contrib import admin
from django.conf import settings
from .models import Agency,Profile,BrokerCategory,BrokerSubCategory,AddPropertyForm
from django.contrib import admin

# default: "Django Administration"
admin.site.site_header = 'RealEstate'
# default: "Site administration"
admin.site.index_title = 'RealEstate | Admin'
# default: "Django site admin"
admin.site.site_title = 'RealEstate'

# Register your models here.
admin.site.register(Agency)
admin.site.register(BrokerCategory)
admin.site.register(BrokerSubCategory)
# here can add user 
admin.site.register(Profile)
admin.site.register(AddPropertyForm)


