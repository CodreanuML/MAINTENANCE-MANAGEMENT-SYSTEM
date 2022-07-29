from GAIA_ASSETS.models import Zona , Asset , SubAsset  , AvarieAsset
from GAIA_ME_CORECTIVA.models import RaportAvarieAsset , RaportAvarieSubAsset
import django_filters
from django_filters import DateFilter ,ModelChoiceFilter


class RAPORT_ASSET_FILTER(django_filters.FilterSet):
	Zona1=Zona.objects.get(nume='Asamblare')
	start_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='gte')
	end_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='lte')
	cauza_avariei=ModelChoiceFilter(queryset=AvarieAsset.objects.filter(Asset__Zona=Zona1))
	class Meta :
		model=RaportAvarieAsset 
		fields='__all__'
		exclude=['Interventie_finalizata','total_subassets','durata_interventie_totala','numar','descriere','activitati_efectuate','Asset','Status','Status_OPEN','Status_Preluat_MNT','Observatii','NUME_MAINT','Cod_Marca_MAINT','NUME_ME_1','Cod_Marca_ME_1','NUME_ME_2','Cod_Marca_ME_2','Semnalat_de_productie','Comunicat_la_intretinere','Interventie_inceputa','durata_interventie']		
		




class RAPORT_SUBASSET_FILTER(django_filters.FilterSet):
	Zona1=Zona.objects.get(nume='Asamblare')
	start_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='gte')
	end_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='lte')
	cauza_avariei=ModelChoiceFilter(queryset=AvarieAsset.objects.filter(Asset__Zona=Zona1))
	class Meta :
		model=RaportAvarieSubAsset 
		fields='__all__'
		exclude=['Interventie_finalizata','numar','descriere','activitati_efectuate','Asset','SubAsset','Status','Status_OPEN','Status_Preluat_MNT','Observatii','NUME_MAINT','Cod_Marca_MAINT','NUME_ME_1','Cod_Marca_ME_1','NUME_ME_2','Cod_Marca_ME_2','Semnalat_de_productie','Comunicat_la_intretinere','Interventie_inceputa','durata_interventie']		




class RAPORT_ASSET_TOP10_FILTER(django_filters.FilterSet):
	start_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='gte')
	end_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='lte')
	class Meta :
		model=RaportAvarieAsset 
		fields='__all__'
		exclude=['Interventie_finalizata','total_subassets','durata_interventie_totala','numar','denumire','cauza_avariei','descriere','activitati_efectuate','Asset','Status','Status_OPEN','Status_Preluat_MNT','Observatii','NUME_MAINT','Cod_Marca_MAINT','NUME_ME_1','Cod_Marca_ME_1','NUME_ME_2','Cod_Marca_ME_2','Semnalat_de_productie','Comunicat_la_intretinere','Interventie_inceputa','durata_interventie']		





class RAPORT_SUBASSET_TOP10_FILTER(django_filters.FilterSet):
	start_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='gte')
	end_date=DateFilter(field_name="Interventie_finalizata", lookup_expr='lte')
	class Meta :
		model=RaportAvarieSubAsset 
		fields='__all__'
		exclude=['Interventie_finalizata','numar','denumire','cauza_avariei','descriere','denumire','cauza_avariei','activitati_efectuate','Asset','SubAsset','Status','Status_OPEN','Status_Preluat_MNT','Observatii','NUME_MAINT','Cod_Marca_MAINT','NUME_ME_1','Cod_Marca_ME_1','NUME_ME_2','Cod_Marca_ME_2','Semnalat_de_productie','Comunicat_la_intretinere','Interventie_inceputa','durata_interventie']		
