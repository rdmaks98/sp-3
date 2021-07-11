from django.db import models

# User_Type = [
#     (0,'user'),
#     (1,'broker'),
# ]

# class User_Profile(models.Model):
#     fname = models.CharField(max_length=200)
#     lname = models.CharField(max_length = 200)
#     mobile = models.CharField(max_length = 200)
# #     User_Type = models.ChoiceField(choices=User_Type, widget=forms.RadioSelect())
#     email = models.EmailField(default = None)
#     # display_picture = models.FileField()

#     def __str__(self):
#         return self.fname




class BrokerCategory(models.Model):
    name = models.CharField(max_length=255)
    # status = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class BrokerSubCategory(models.Model):
    sub_category = models.ForeignKey(BrokerCategory, on_delete= models.CASCADE)
    sub_name = models.CharField(max_length=255)
    def __str__(self):
        return self.sub_name