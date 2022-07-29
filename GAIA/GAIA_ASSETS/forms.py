from django import forms
from .models import Asset , SubAsset , AvarieAsset

class NewAssetForm(forms.ModelForm):
	denumire =forms.CharField(widget=forms.Textarea(), max_length=30, help_text='Denumirea Liniei de Productie- Maxim 30 caractere')  
	subasset_val = forms.BooleanField(initial=False, required=False,  help_text='Bifati daca Linia contine statii de lucru',label='Statii de Lucru')      
	ID_Asset = forms.CharField(widget=forms.Textarea(), max_length=50, help_text='OP-ul aferent Liniei',label='OP Linie Productie')  
	status=forms.BooleanField(initial=False, required=False, help_text='Bifati daca Linia se afla sau nu in exploatare') 



	class Meta :
		model=Asset 
		fields=['denumire','subasset_val','ID_Asset','status']
		



class NewSubAssetForm(forms.ModelForm):
	denumire =forms.CharField(widget=forms.Textarea(), max_length=30, help_text='Denumirea Statiei de Lucru- Maxim 30 caractere')       
	ID_SubAsset = forms.CharField(widget=forms.Textarea(), max_length=50, help_text='OP-ul aferent statiei de lucru',label='OP Statie Lucru')  
	status=forms.BooleanField(initial=False, required=False, help_text='Bifati daca Statia se afla sau nu in exploatare') 

	class Meta :
		model=SubAsset
		fields=['denumire','ID_SubAsset','status']






class NewAvarieForm(forms.ModelForm):
	denumire=forms.CharField(max_length=30,label = 'Denumirea Avariei') 


	class Meta :
		model=AvarieAsset
		fields=['denumire']





