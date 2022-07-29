from django import forms
from .models import  Location , Item


class Form_add_location(forms.ModelForm):
	nume=forms.CharField(max_length=30,label='Denumire Locatie')

	class Meta :
		model=Location
		fields=['nume']



class Form_add_item(forms.ModelForm):
	nume=forms.CharField(max_length=70,label='Denumire Obiect')

	part_no=forms.CharField(max_length=70,label='Part Number')
	location=forms.ModelChoiceField(queryset=Location.objects.all(),label='Locatie')
	stock_qty=forms.IntegerField(label='Cantitate in stoc')
	unit_price=forms.FloatField(label='Pret unitar')
	minimun_stock_qty=forms.IntegerField(label='Stoc minim')
	maximum_stock_qty=forms.IntegerField(label='Stoc maxim')
	critical=forms.BooleanField(label='Piesa este critica ')
	class Meta :
		model=Item
		fields=['nume','part_no','location','stock_qty','unit_price','minimun_stock_qty','maximum_stock_qty','critical']