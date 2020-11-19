from django.db import models
# Create your models here.


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Stuff(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
