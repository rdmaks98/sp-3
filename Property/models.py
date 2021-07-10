from django.db import models
from phone_field import PhoneField

# add agency model create
class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    mobile = models.CharField(max_length=40)
    image = models.ImageField(upload_to="Property/images/",default="")

    def __str__(self):
        return self.name

# broker model
class Broker(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    mobile = PhoneField(blank=True, help_text='Contact phone number')
    image = models.ImageField(upload_to="Property/images/profile",default="")
    user = (('user','user'),
            ('broker','broker'))
    user_type = models.CharField(max_length=10,choices=user,default="user")

    def __str__(self):
        return self.name + " " + self.user_type

