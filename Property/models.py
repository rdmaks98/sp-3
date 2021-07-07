from django.db import models
class Agency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    mobile = models.CharField(max_length=40)
    image = models.ImageField(upload_to="Property/images/",default="")

    def __str__(self):
        return self.name