from django.db import models


# Create your models here.
class registration(models.Model):
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)


    def __str__(self):
        return self.Firstname + '  ' + self.Lastname + '    ' + self.Email
