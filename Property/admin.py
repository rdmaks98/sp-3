from django.contrib import admin
from django.conf import settings
from .models import Agency,UserProfile,BrokerCategory,BrokerSubCategory,AddPropertyForm,Rating
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
admin.site.register(AddPropertyForm)
admin.site.register(Rating)
# here we can add user 
admin.site.register(UserProfile)



