from django.db import models

# database model 
class Record(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

 
def __str__(self):
    return (f"{self.name} {self.email} {self.password} {self.country}")
