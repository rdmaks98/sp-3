from django.db import models
from phone_field import PhoneField
import datetime
from django.contrib.auth.models import User


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
        # return self.name
        return self.sub_name


class Agency(models.Model):
    id = models.IntegerField(primary_key=True,default="")
    u_id = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    a_name = models.CharField(max_length=200,default="")
    a_image = models.ImageField(upload_to="Property/images/agency/",default="")
    a_address = models.CharField(max_length=200,default="")

    def __str__(self): 
        return self.all
