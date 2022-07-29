

# Create your views here.
from django.shortcuts import render , redirect, get_object_or_404 
from django.http import HttpResponse
from GAIA_ASSETS.models import Zona , Asset , SubAsset  , AvarieAsset
from GAIA_ME_CORECTIVA.models import RaportAvarieAsset , RaportAvarieSubAsset
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import pytz
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
utc=pytz.UTC
from .filters import RAPORT_ASSET_FILTER ,RAPORT_SUBASSET_FILTER, RAPORT_ASSET_TOP10_FILTER , RAPORT_SUBASSET_TOP10_FILTER





@login_required
def main(request,nume_zona):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :

			nume_zona='Asamblare'

		Zona1=Zona.objects.get(nume=nume_zona)
		return render(request,'GAIA_RAPORTARI/main.html',{'Zona':Zona1})


	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')

@login_required
def main_filtru_rapoarte_data_assets(request,nume_zona):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs
		page=request.GET.get('page',1)
		paginator=Paginator(queryset,10)
		try:
			Rapoarte_called=paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			Rapoarte_called=paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			Rapoarte_called=paginator.page(paginator.num_pages)




		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_DATE_ASSET.html',{'myFilter':myFilter,'Rapoarte_called':Rapoarte_called,'Zona':Zona1})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def main_filtru_rapoarte_data_subassets(request,nume_zona):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'


		Zona_called=Zona.objects.get(nume=nume_zona)
		RaportAvarieSubAsset1=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')	
		myFilter=RAPORT_SUBASSET_FILTER(request.POST,queryset=RaportAvarieSubAsset1)
		queryset=myFilter.qs
		page=request.GET.get('page',1)
		paginator=Paginator(queryset,10)
		try:
			Rapoarte_called=paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			Rapoarte_called=paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			Rapoarte_called=paginator.page(paginator.num_pages)

		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_DATE_SUBASSET.html',{'myFilter':myFilter,'Rapoarte_called':Rapoarte_called,'Zona':Zona_called})


	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def main_filtru_rapoarte_top10_assets(request,nume_zona):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

		Zona1=Zona.objects.get(nume=nume_zona)

		RaportAvarieAsset1=RaportAvarieAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs
		Rapoarte_called=queryset.order_by('-durata_interventie_totala')[0:10]




		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_TOP10_ASSET.html',{'myFilter':myFilter,'Rapoarte_called':Rapoarte_called,'Zona':Zona1})


	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def main_filtru_rapoarte_top10_subassets(request,nume_zona):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

		Zona_called=Zona.objects.get(nume=nume_zona)
		RaportAvarieSubAsset1=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')	
		myFilter=RAPORT_SUBASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieSubAsset1)
		queryset=myFilter.qs
		Rapoarte_called=queryset.order_by('-durata_interventie')[0:10]



		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_TOP10_SUBASSET.html',{'myFilter':myFilter,'Rapoarte_called':Rapoarte_called,'Zona':Zona_called})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def main_filtru_rapoarte_top10_recurenta_assets(request,nume_zona):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs

		AvarieAsset1=AvarieAsset.objects.filter(Asset__Zona=Zona1)
		report={}
		for avarie in AvarieAsset1:
			count1=queryset.filter(cauza_avariei=avarie).count()
			report[avarie.denumire]=count1

		sort_order=sorted(report.items(), key=lambda x: x[1], reverse=True)
	
		sort_orders=sort_order[0:12]



		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_TOP10_RECURENTA_ASSET.html',{'myFilter':myFilter,'Top10':sort_orders,'Zona':Zona1})



	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def main_filtru_rapoarte_top10_recurenta_subassets(request,nume_zona):



	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :




		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'


		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_SUBASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs

		AvarieAsset1=AvarieAsset.objects.filter(Asset__Zona=Zona1)
		report={}
		for avarie in AvarieAsset1:
			count1=queryset.filter(cauza_avariei=avarie).count()
			report[avarie.denumire]=count1

		sort_order=sorted(report.items(), key=lambda x: x[1], reverse=True)
	
		sort_orders=sort_order[0:12]



		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_TOP10_RECURENTA_SUBASSET.html',{'myFilter':myFilter,'Top10':sort_orders,'Zona':Zona1})


	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')







@login_required
def main_filtru_rapoarte_MTBF_assets(request,nume_zona):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'


		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs
		Asset1=Asset.objects.filter(Zona=Zona1)
		report={}
		for asset in Asset1 :
			count1=queryset.filter(Asset=asset).count()
			report[asset.denumire]=count1

		sort_orders=sorted(report.items(), key=lambda x: x[1], reverse=True)

		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_MTBF_ASSET.html',{'myFilter':myFilter,'MTBF':sort_orders,'Zona':Zona1})


	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')






@login_required
def main_filtru_rapoarte_MTBF_subassets(request,nume_zona):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs
		SubAsset1=SubAsset.objects.filter(Asset__Zona=Zona1)
		report={}
		for asset in SubAsset1 :
			count1=queryset.filter(SubAsset=asset).count()
			report[asset.denumire]=count1

		sort_orders=sorted(report.items(), key=lambda x: x[1], reverse=True)

		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_MTBF_SUBASSET.html',{'myFilter':myFilter,'MTBF':sort_orders,'Zona':Zona1})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def main_filtru_rapoarte_MTTR_assets(request,nume_zona):
	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs
		Asset1=Asset.objects.filter(Zona=Zona1)
		report={}
		for asset in Asset1 :

		
			Rapoarte_Asset=queryset.filter(Asset=asset)
			count=0
			for raport in Rapoarte_Asset :

				count+=raport.durata_interventie_totala

			report[asset.denumire]=count

		sort_orders=sorted(report.items(), key=lambda x: x[1], reverse=True)

		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_MTTR_ASSET.html',{'myFilter':myFilter,'MTBF':sort_orders,'Zona':Zona1})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def main_filtru_rapoarte_MTTR_subassets(request,nume_zona):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		if nume_zona not in ['Asamblare','Airbag','Diecasting','Foaming','IMO','LW','Toolshop'] :
		
			nume_zona='Asamblare'

	
		Zona1=Zona.objects.get(nume=nume_zona)
		RaportAvarieAsset1=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona1).order_by('-numar')
		myFilter=RAPORT_ASSET_TOP10_FILTER(request.POST,queryset=RaportAvarieAsset1)
		queryset=myFilter.qs
		SubAsset1=SubAsset.objects.filter(Asset__Zona=Zona1)
		report={}
		for asset in SubAsset1 :

		
			Rapoarte_SubAsset=queryset.filter(SubAsset=asset)
			count=0
			for raport in Rapoarte_SubAsset :

				count+=raport.durata_interventie

			report[asset.denumire]=count

		sort_orders=sorted(report.items(), key=lambda x: x[1], reverse=True)

		return render(request,'GAIA_RAPORTARI/RAPORTARI_FILTRU_MTTR_SUBASSET.html',{'myFilter':myFilter,'MTBF':sort_orders,'Zona':Zona1})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')
