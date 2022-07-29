from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Employee(models.Model):


    DEP_CHOICES = [
        ('Productie', 'Productie'),
        ('Mentenanta', 'Mentenanta'),
        ('Admin' , 'Admin'),

    ]


    ZONA_CHOICES = [
        ('Asamblare', 'Asamblare'),
        ('Airbag', 'Airbag'),
        ('Foaming' , 'Foaming'),
        ('Diecasting' , 'Diecasting'),
        ('LW' , 'LW'),
        ('IMO' , 'IMO'),
        ('Toolshop' , 'Toolshop'),
        ('Toate' , 'Toate'),

    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, choices=DEP_CHOICES)
    Zona = models.CharField(max_length=100, choices=ZONA_CHOICES)


    def __str__(self):
        return self.user.username