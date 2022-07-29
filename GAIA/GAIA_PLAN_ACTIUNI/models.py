from django.db import models
from GAIA_ASSETS.models import Zona
from GAIA_ACCOUNTS.models import Employee
import datetime


# Create your models here.


class Actiune(models.Model):
	denumire=models.CharField(unique=True,max_length=50)
	cauza=models.CharField(max_length=100)
	Actiune=models.CharField(max_length=100)
	responsabil=models.ManyToManyField(Employee)

	status_choice = [
        ('I', 'Actiune nefinalizata la timp'),
        ('O', 'Actiune in desfasurare'),
        ('C', 'Actiune incheiata'),
        ('E', 'Actiune incheiata eficace'),
        
    ]

	status=models.CharField(choices=status_choice,max_length=1)

	hide_date=models.DateField(default=datetime.datetime.now())
	data_deschidre_actiune=models.CharField(max_length=10)
	data_preconizare_finalizare=models.CharField(max_length=10)
	data_finaliarii=models.CharField(max_length=10,blank=True)
	data_verificarii_eficientei=models.CharField(max_length=10,blank=True)
	comentarii=models.TextField(max_length=100)
	zona=models.ForeignKey(Zona, related_name='Zona_Actiune',on_delete=models.CASCADE)


	def __str__(self):
		return self.denumire 


	class Meta:
		ordering=['-hide_date']