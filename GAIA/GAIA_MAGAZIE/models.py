from django.db import models

# Create your models here.


class Location(models.Model):
	nume=models.CharField(max_length=30,unique=True)

	def __str__(self):
		return self.nume

	class Meta:
		ordering=['nume']



class Item(models.Model):
	nume=models.CharField(max_length=70,unique=True)

	part_no=models.CharField(max_length=70,unique=True)
	location=models.ForeignKey(Location,on_delete=models.CASCADE)
	stock_qty=models.IntegerField()
	unit_price=models.FloatField()
	minimun_stock_qty=models.IntegerField()
	maximum_stock_qty=models.IntegerField()
	critical=models.BooleanField()

	def __str__(self):
		return self.nume

