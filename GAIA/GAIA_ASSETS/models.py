from django.db import models
from datetime import datetime

# Create your models here.


class Zona(models.Model):
    nume = models.CharField(max_length=30, unique=True)  # """ NUMELE ZONELOR DE PRODUCTIE """
    descriere = models.CharField(max_length=100)		 # """ DESCRIEREA ZONELOR DE PRODUCTIE """		

    def __str__(self):
    	return self.nume

class Asset(models.Model): 
    denumire = models.CharField(max_length=80)   # """ NUMELE ECHIPAMENTULUI / RESPECTIV ANSAMBLU DE ECHIPAMENTE """
    subasset_val = models.BooleanField()         # """ DACA ARE SA NU SUBANSAMBLE 0y=NU ARE / 1=ARE """
    data_adaugare = models.DateTimeField(auto_now_add=True)  # """ DATA ADAUGARE ECHIPAMENT """
    Zona = models.ForeignKey(Zona, related_name='Zona',on_delete=models.CASCADE)  # """ ZONA IN CARE SE AFLA ECHIPAMENTUL """
    ID_Asset = models.CharField(max_length=30, unique=True)  # """ ID ECHIPAMENT """
    status=models.BooleanField()  # """ STATUSUL ECHIPAMENTULUI 0=inactiv(nu se explpateaza) /  1=activ(este in exploatare) """

    def __str__(self):
    	return self.denumire


class SubAsset(models.Model):
	denumire=models.CharField(max_length=80)  # """ NUMELE SUBANSAMBLULUI """
	Asset=models.ForeignKey(Asset, related_name='Asset', on_delete=models.CASCADE)  # """ ASSETUL DIN CARE FACE PARTE"""
	data_adaugare=models.DateTimeField(auto_now_add=True) # """ DATA ADAUGARE ECHIPAMENT """
	ID_SubAsset=models.CharField(max_length=30, unique=True)  # """ ID ECHIPAMENT """
	status=models.BooleanField(default=0)	
	def __str__(self):
		return self.denumire


class AvarieAsset(models.Model):
    denumire=models.CharField(max_length=30)
    Asset=models.ForeignKey(Asset, related_name='Asset_avarie', on_delete=models.CASCADE)


    def __str__(self):
        return self.denumire

