from django.db import models
from phone_field import PhoneField
import datetime

# add agency model create
class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    mobile = models.CharField(max_length=40)
    image = models.ImageField(upload_to="Property/images/",default="")

    def __str__(self):
        return self.name

# user profile 
class Profile(models.Model):
    u_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    profile = models.ImageField(upload_to="Property/images/profile",default="")
    user = (('user','user'),
            ('broker','broker'))
    user_type = models.CharField(max_length=10,choices=user,default="user")
    details = models.CharField(max_length=200)
    dob = models.DateField(("Date"),default=datetime.date.today)
    
    def __str__(self):
        return self.name + " " + self.user_type 

class BrokerCategory(models.Model):
    name = models.CharField(max_length=255)
    # status = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class BrokerSubCategory(models.Model):
    sub_category = models.ForeignKey(BrokerCategory, on_delete= models.CASCADE)
    sub_name = models.CharField(max_length=255)
    def __str__(self):
# <<<<<<< HEAD
# =======
#         # return self.name
# >>>>>>> origin/aakash
        return self.sub_name

class AddPropertyForm(models.Model):
    #property_Details
    propertyTitle = models.CharField(max_length=255)
    propertyType = models.CharField(max_length=255)#Dropdown
    price = models.CharField(max_length=255)
    propertyDescription = models.CharField(max_length=255)

    #property_location
    address = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    Neighborhood = models.CharField(max_length=255)
    Country = models.CharField(max_length=255) #Dropdown
    
    #Property Features
    areasize = models.CharField(max_length=255)
    sizeprefix = models.CharField(max_length=255)
    landarea = models.CharField(max_length=255)
    landAreaSize = models.CharField(max_length=255)
    bedrooms = models.CharField(max_length=255)
    bathrooms = models.CharField(max_length=255)
    builtyear = models.CharField(max_length=255)
    propertyimage = models.ImageField(upload_to="Property/images/property",default="")

    def __str__(self):
        return self.propertyTitle
