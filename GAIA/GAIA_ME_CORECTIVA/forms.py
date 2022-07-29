from django import forms
from .models import  RaportAvarieAsset   , RaportAvarieSubAsset
from GAIA_ASSETS.models import AvarieAsset


#FORMS pentru RAPORT NOU AVARIE ASSET

class NewRaportAsset00Form(forms.ModelForm):
	denumire=forms.CharField(max_length=50,label = 'Denumirea Raportului') 
	Cod_Marca_ME_1=forms.IntegerField(label = 'Numar Marca Initiator Raport Avarie') 


	class Meta :
		model=RaportAvarieAsset
		fields=['denumire','Cod_Marca_ME_1']
	
class NewRaportAsset01Form(forms.ModelForm):
	descriere=forms.CharField(max_length=80,label ='Descrierea Raportului de avarie') 
	cauza_avariei= forms.ChoiceField()
	activitati_efectuate=forms.CharField(max_length=80,label ='Activitati efectuate') 
	Cod_Marca_MAINT=forms.IntegerField(label ='Cod Marca Tehnician Mentenanta') 


	class Meta :
		model=RaportAvarieAsset
		fields=['descriere','cauza_avariei','activitati_efectuate','Cod_Marca_MAINT']

class NewRaportAsset11Form(forms.ModelForm):
	Observatii=forms.CharField(max_length=80,label ='Observatii Raport de avarie')
	Cod_Marca_ME_2=forms.IntegerField(label = 'Numar Marca Persoanei Aprobare Inchidere Avarie') 


	class Meta :
		model=RaportAvarieAsset
		fields=['Observatii','Cod_Marca_ME_2']


#FORMS pentru RAPORT NOU AVARIE SUBASSET


class NewRaportSubAsset00Form(forms.ModelForm):
	denumire=forms.CharField(max_length=50,label = 'Denumirea Raportului') 
	Cod_Marca_ME_1=forms.IntegerField(label = 'Numar Marca Initiator Raport Avarie') 


	class Meta :
		model=RaportAvarieSubAsset
		fields=['denumire','Cod_Marca_ME_1']



class NewRaportSubAsset01Form(forms.ModelForm):
	descriere=forms.CharField(max_length=80,label ='Descrierea Raportului de avarie') 
	cauza_avariei= forms.ChoiceField()
	activitati_efectuate=forms.CharField(max_length=80,label ='Activitati efectuate') 
	Cod_Marca_MAINT=forms.IntegerField(label ='Cod Marca Tehnician Mentenanta') 


	class Meta :
		model=RaportAvarieSubAsset
		fields=['descriere','cauza_avariei','activitati_efectuate','Cod_Marca_MAINT']



class NewRaportSubAsset11Form(forms.ModelForm):
	Observatii=forms.CharField(max_length=80,label ='Observatii Raport de avarie')
	Cod_Marca_ME_2=forms.IntegerField(label = 'Numar Marca Persoanei Aprobare Inchidere Avarie') 


	class Meta :
		model=RaportAvarieSubAsset
		fields=['Observatii','Cod_Marca_ME_2']