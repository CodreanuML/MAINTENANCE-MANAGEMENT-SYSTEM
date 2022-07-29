from django.shortcuts import render , redirect, get_object_or_404 
from django.http import HttpResponse
from GAIA_ASSETS.models import Zona , Asset , SubAsset  , AvarieAsset
from .models import RaportAvarieAsset , RaportAvarieSubAsset
# Create your views here.
from .forms import NewRaportAsset00Form , NewRaportAsset01Form , NewRaportAsset11Form , NewRaportSubAsset00Form , NewRaportSubAsset01Form , NewRaportSubAsset11Form
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import pytz
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
utc=pytz.UTC



#INSTATIERE RAPORT DE AVARIE - AIRBAG VIEW

#MAIN PAGE PRODUCTIE 
@login_required
def home_productie(request) :
    
    current_user_department = request.user.employee.department
    
    if current_user_department == 'Productie' or current_user_department == 'Admin' :


        RaportAvarieAsset_deschis_ME=RaportAvarieAsset.objects.filter(Status_OPEN=0)
        RaportAvarieAsset_deschis_MNT=RaportAvarieAsset.objects.filter(Status_OPEN=1,Status=0)
        RaportAvarieSubAsset_deschis_ME=RaportAvarieSubAsset.objects.filter(Status_OPEN=0)
        RaportAvarieSubAsset_deschis_MNT=RaportAvarieSubAsset.objects.filter(Status_OPEN=1,Status=0)
        return render(request,'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_PRODUCTIE_MAIN.html',{'RaportAvarie_deschis_ME':RaportAvarieAsset_deschis_ME,'RaportAvarie_deschis_MNT':RaportAvarieAsset_deschis_MNT,'RaportAvarieSubAsset_deschis_ME':RaportAvarieSubAsset_deschis_ME,'RaportAvarieSubAsset_deschis_MNT':RaportAvarieSubAsset_deschis_MNT})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')    


# ASAMBLARE
@login_required
def me_corectiva_asamblare(request) :
   
    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Asamblare') or current_user_department == 'Admin'  :



        Zona1=Zona.objects.get(nume='Asamblare')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request,'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_ASAMBLARE_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 

    #subansamble 
@login_required
def me_corectiva_asamblare_subasset(request,pk):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Asamblare') or current_user_department == 'Admin'  :



        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_ASAMBLARE_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 


@login_required
def me_corectiva_asamblare_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Asamblare') or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='Asamblare')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_ASAMBLARE_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 


@login_required
def me_corectiva_asamblare_rapoarte_subassets(request):


    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Asamblare') or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='Asamblare')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_ASAMBLARE_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 



@login_required
def mnt_corectiva_asamblare_rapoarte(request):


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Asamblare')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_ASAMBLARE_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 




@login_required
def mnt_corectiva_asamblare_rapoarte_subassets(request):



    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta'  or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='Asamblare')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_ASAMBLARE_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 


# AIRBAG
@login_required
def me_corectiva_airbag(request) :

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Airbag') or current_user_department == 'Admin'  :


        Zona1=Zona.objects.get(nume='Airbag')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_AIRBAG_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 


    #subansamble 
@login_required
def me_corectiva_airbag_subasset(request,pk):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Airbag') or current_user_department == 'Admin'  :

        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_AIRBAG_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 




@login_required
def me_corectiva_airbag_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Airbag') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Airbag')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_AIRBAG_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 


@login_required
def me_corectiva_airbag_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Airbag') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Airbag')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_AIRBAG_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 


@login_required
def mnt_corectiva_airbag_rapoarte(request):

    
    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='Airbag')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_AIRBAG_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 





@login_required
def mnt_corectiva_airbag_rapoarte_subassets(request):

    
    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta'  or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Airbag')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_AIRBAG_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 



# DC
@login_required
def me_corectiva_diecasting(request) :

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Diecasting') or current_user_department == 'Admin'  :


        Zona1=Zona.objects.get(nume='Diecasting')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_DIECASTING_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 




    #subansamble 
@login_required
def me_corectiva_diecasting_subasset(request,pk):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Diecasting') or current_user_department == 'Admin'  :


        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_DIECASTING_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 





@login_required
def me_corectiva_diecasting_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Diecasting') or current_user_department == 'Admin'  :




        Zona_called=Zona.objects.get(nume='Diecasting')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_DIECASTING_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html') 



@login_required
def me_corectiva_diecasting_rapoarte_subassets(request):


    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Diecasting') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Diecasting')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_DIECASTING_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')





@login_required
def mnt_corectiva_diecasting_rapoarte(request):

    
    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Diecasting')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_DIECASTING_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def mnt_corectiva_diecasting_rapoarte_subassets(request):


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta'  or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Diecasting')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_DIECASTING_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


# FOAMING
@login_required
def me_corectiva_foaming(request) :

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Foaming') or current_user_department == 'Admin'  :




        Zona1=Zona.objects.get(nume='Foaming')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_FOAMING_MAIN.html',{'Assets':Assets})



    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



    #subansamble 
@login_required
def me_corectiva_foaming_subasset(request,pk):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Foaming') or current_user_department == 'Admin'  :



        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_FOAMING_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def me_corectiva_foaming_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Foaming') or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='Foaming')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_FOAMING_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def me_corectiva_foaming_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Foaming') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Foaming')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_FOAMING_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')






@login_required
def mnt_corectiva_foaming_rapoarte(request):

    
    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta'  or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='Foaming')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_FOAMING_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def mnt_corectiva_foaming_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :




        Zona_called=Zona.objects.get(nume='Foaming')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_FOAMING_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



# IMO
@login_required
def me_corectiva_imo(request) :

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='IMO') or current_user_department == 'Admin'  :



        Zona1=Zona.objects.get(nume='IMO')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_IMO_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


    #subansamble 
@login_required
def me_corectiva_imo_subasset(request,pk):


    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='IMO') or current_user_department == 'Admin'  :



        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_IMO_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def me_corectiva_imo_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='IMO') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='IMO')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_IMO_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def me_corectiva_imo_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='IMO') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='IMO')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_IMO_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def mnt_corectiva_imo_rapoarte(request):

    current_user_department = request.user.employee.department
    

    if current_user_department == 'Mentenanta'  or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='IMO')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_IMO_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def mnt_corectiva_imo_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='IMO')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_IMO_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')





# LW
@login_required
def me_corectiva_lw(request) :

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='LW') or current_user_department == 'Admin'  :


        Zona1=Zona.objects.get(nume='LW')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request,'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_LW_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

    #subansamble 
@login_required
def me_corectiva_lw_subasset(request,pk):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='LW') or current_user_department == 'Admin'  :


        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_LW_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def me_corectiva_lw_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='LW') or current_user_department == 'Admin'  :


        Zona_called=Zona.objects.get(nume='LW')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request,'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_LW_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')





@login_required
def me_corectiva_lw_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='LW') or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='LW')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_LW_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def mnt_corectiva_lw_rapoarte(request):

    
    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta'  or current_user_department == 'Admin'  :




        Zona_called=Zona.objects.get(nume='LW')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_LW_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')





@login_required
def mnt_corectiva_lw_rapoarte_subassets(request):

    
    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :




        Zona_called=Zona.objects.get(nume='LW')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_LW_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')





# TOOLSHOP
@login_required
def me_corectiva_toolshop(request) :


    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Toolshop') or current_user_department == 'Admin'  :



        Zona1=Zona.objects.get(nume='Toolshop')
        queryset=Asset.objects.filter(Zona=Zona1)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Assets = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Assets = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Assets = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_TOOLSHOP_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

    #subansamble 
@login_required
def me_corectiva_toolshop_subasset(request,pk):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Toolshop') or current_user_department == 'Admin'  :




        Asset_called=Asset.objects.get(pk=pk)
        queryset=SubAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            SubAsset_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            SubAsset_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           SubAsset_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_TOOLSHOP_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def me_corectiva_toolshop_rapoarte(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Toolshop') or current_user_department == 'Admin'  :


 


        Zona_called=Zona.objects.get(nume='Toolshop')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_TOOLSHOP_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def me_corectiva_toolshop_rapoarte_subassets(request):

    current_user_department = request.user.employee.department
    current_user_zona=request.user.employee.Zona

    if ( current_user_department == 'Productie' and current_user_zona=='Toolshop') or current_user_department == 'Admin'  :


 


        Zona_called=Zona.objects.get(nume='Toolshop')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_TOOLSHOP_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def mnt_corectiva_toolshop_rapoarte(request):

    current_user_department = request.user.employee.department
    

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin':
        Zona_called=Zona.objects.get(nume='Toolshop')
        queryset=RaportAvarieAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_TOOLSHOP_RAPOARTE.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def mnt_corectiva_toolshop_rapoarte_subassets(request):

    current_user_department = request.user.employee.department


    if current_user_department == 'Mentenanta' or current_user_department == 'Admin'  :



        Zona_called=Zona.objects.get(nume='Toolshop')
        queryset=RaportAvarieSubAsset.objects.filter(Asset__Zona=Zona_called).order_by('-numar')
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)
        try:
            Rapoarte_called = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Rapoarte_called = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
           Rapoarte_called= paginator.page(paginator.num_pages)
        
        return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_TOOLSHOP_RAPOARTE_SUBASSET.html',{'Rapoarte_called':Rapoarte_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

























#RAPORT NOU AVARIE  ASSET

def getno() :                                 # functie ajutatoare pentru a obtine numarul raportului curent de avarie
     numar1=RaportAvarieAsset.objects.all().count()
     numar2=RaportAvarieSubAsset.objects.all().count()
     return numar1+numar2+1


     


@login_required
def NewRaportAsset00VIEW(request,pk):
    Asset_val=Asset.objects.get(pk=pk )
    current_user_name = request.user.username


    numar=getno()
    


    if request.method=='POST':

        form=NewRaportAsset00Form(request.POST)
        if form.is_valid() :

            RaportAvarieAsset=form.save(commit=False)
            RaportAvarieAsset.Semnalat_de_productie=datetime.now()
            RaportAvarieAsset.Comunicat_la_intretinere=datetime.now()
            RaportAvarieAsset.NUME_ME_1=current_user_name
            RaportAvarieAsset.numar=numar
            RaportAvarieAsset.Asset=Asset_val
            RaportAvarieAsset.Status=0
            RaportAvarieAsset.Status_OPEN=0
            RaportAvarieAsset.save()
           
            return redirect('phome' )

    else:

            form=NewRaportAsset00Form()

    return render (request, 'GAIA_ME_CORECTIVA_TEMPLATES/RAPORT_ASSET_NEW_0.0.html',{'form':form, 'Asset':Asset_val })



#confirmare preluare avarie
@login_required
def NewRaportAsset001VIEW(request,pk):
    RaportAvarie=RaportAvarieAsset.objects.get(pk=pk)
            
    RaportAvarie.Status_Preluat_MNT=1 
            
    
    RaportAvarie.Interventie_inceputa=datetime.now()


    RaportAvarie.save()

    return redirect('mhome' )



#finalizare raport MNT
@login_required
def NewRaportAsset01VIEW(request,pk):
    RaportAvarie=RaportAvarieAsset.objects.get(pk=pk)
    ASSET=RaportAvarie.Asset
    queryset=AvarieAsset.objects.filter(Asset=ASSET)
    total_subassets_c=SubAsset.objects.filter(Asset=ASSET).count()
    #ADDED NEW TO NOT BE ABLE TO EDIT

    #ADDED NEW TO NOT BE ABLE TO EDIT


    current_user_name = request.user.username

    if RaportAvarie.Status_OPEN==1  :
        return redirect('mhome' )
        

    ###########################

    if request.method=='POST':

        form=NewRaportAsset01Form(request.POST)
        if form.is_valid() :
            
            RaportAvarie.descriere=form.cleaned_data['descriere']
            RaportAvarie.cauza_avariei=form.cleaned_data['cauza_avariei']
            RaportAvarie.activitati_efectuate=form.cleaned_data['activitati_efectuate']
            RaportAvarie.NUME_MAINT=current_user_name
            RaportAvarie.Cod_Marca_MAINT=form.cleaned_data['Cod_Marca_MAINT']
            RaportAvarie.Status_OPEN=1
            RaportAvarie.Status=0
            RaportAvarie.Interventie_finalizata=datetime.now()

            then=RaportAvarie.Interventie_inceputa.replace(tzinfo=utc)
            now=RaportAvarie.Interventie_finalizata.replace(tzinfo=utc)
            duration=now - then
            duration_sec=duration.total_seconds() 
            duration_min=duration_sec/60
            RaportAvarie.durata_interventie=duration_min
            RaportAvarie.total_subassets=total_subassets_c
            RaportAvarie.durata_interventie_totala=duration_min*total_subassets_c
            RaportAvarie.save()

            return redirect('mhome' )

    else:
        NewRaportAsset01Form.base_fields['cauza_avariei'] = forms.ModelChoiceField(queryset= queryset)
        form=NewRaportAsset01Form()

 
    return render (request, 'GAIA_ME_CORECTIVA_TEMPLATES/RAPORT_ASSET_NEW_0.1.html',{'form':form, 'Raport':RaportAvarie })    


#Introducere masina productie
@login_required
def NewRaportAsset11VIEW(request,pk):

    RaportAvarie=RaportAvarieAsset.objects.get(pk=pk)

    current_user_name = request.user.username
    #ADDED NEW TO NOT BE ABLE TO EDIT

    if RaportAvarie.Status==1  :
        return redirect('phome' )
        

    ###########################


    if request.method=='POST':

        form=NewRaportAsset11Form(request.POST)
        if form.is_valid() :

            RaportAvarie.Observatii=form.cleaned_data['Observatii']
            RaportAvarie. NUME_ME_2=current_user_name
            RaportAvarie.Cod_Marca_ME_2=form.cleaned_data['Cod_Marca_ME_2']
            RaportAvarie.Status_OPEN=1
            RaportAvarie.Status=1


            RaportAvarie.save()
            return redirect('phome' )

    else:

        form=NewRaportAsset11Form()

 
    return render (request, 'GAIA_ME_CORECTIVA_TEMPLATES/RAPORT_ASSET_NEW_1.1.html',{'form':form, 'Raport':RaportAvarie })

#RAPORT NOU AVARIE  SUBASSET
@login_required
def NewRaportSubAsset00VIEW(request,Asset_pk,pk):
    Asset_val=Asset.objects.get(pk=Asset_pk )
    SubAsset_val=SubAsset.objects.get(pk=pk)

    current_user_name = request.user.username
    numar=getno()
    

    if request.method=='POST':

        form=NewRaportSubAsset00Form(request.POST)
        if form.is_valid() :

            RaportAvarieSubAsset=form.save(commit=False)
            RaportAvarieSubAsset.NUME_ME_1=current_user_name
            RaportAvarieSubAsset.numar=numar
            RaportAvarieSubAsset.Semnalat_de_productie=datetime.now()
            RaportAvarieSubAsset.Comunicat_la_intretinere=datetime.now()
            RaportAvarieSubAsset.Asset=Asset_val
            RaportAvarieSubAsset.SubAsset=SubAsset_val
            RaportAvarieSubAsset.Status=0
            RaportAvarieSubAsset.Status_OPEN=0
            RaportAvarieSubAsset.save()
           
            return redirect('phome' )

    else:

            form=NewRaportSubAsset00Form()

    return render (request, 'GAIA_ME_CORECTIVA_TEMPLATES/RAPORT_SUBASSET_NEW_0.0.html',{'form':form, 'Asset':Asset_val , 'SubAsset':SubAsset_val })



#confirmare preluare avarie
@login_required
def NewRaportSubAsset001VIEW(request,pk):
    RaportAvarie=RaportAvarieSubAsset.objects.get(pk=pk)
            
    RaportAvarie.Status_Preluat_MNT=1 
            
    
    RaportAvarie.Interventie_inceputa=datetime.now()


    RaportAvarie.save()

    return redirect('mhome' )



#finalizare raport MNT
@login_required
def NewRaportSubAsset01VIEW(request,pk):
    RaportAvarie=RaportAvarieSubAsset.objects.get(pk=pk)
    ASSET=RaportAvarie.Asset
    queryset=AvarieAsset.objects.filter(Asset=ASSET)
    current_user_name = request.user.username

    if RaportAvarie.Status_OPEN==1  :
        return redirect('mhome' )
        

    ###########################


    if request.method=='POST':

        form=NewRaportSubAsset01Form(request.POST)
        if form.is_valid() :
            
            RaportAvarie.descriere=form.cleaned_data['descriere']
            RaportAvarie.cauza_avariei=form.cleaned_data['cauza_avariei']
            RaportAvarie.activitati_efectuate=form.cleaned_data['activitati_efectuate']
            RaportAvarie.NUME_MAINT=current_user_name
            RaportAvarie.Cod_Marca_MAINT=form.cleaned_data['Cod_Marca_MAINT']
            RaportAvarie.Status_OPEN=1
            RaportAvarie.Status=0
            RaportAvarie.Interventie_finalizata=datetime.now()

            then=RaportAvarie.Interventie_inceputa.replace(tzinfo=utc)
            now=RaportAvarie.Interventie_finalizata.replace(tzinfo=utc)
            duration=now - then
            duration_sec=duration.total_seconds() 
            duration_min=duration_sec/60
            RaportAvarie.durata_interventie=duration_min

           
            
            RaportAvarie.save()

            return redirect('mhome' )

    else:
        NewRaportSubAsset01Form.base_fields['cauza_avariei'] = forms.ModelChoiceField(queryset= queryset)
        form=NewRaportSubAsset01Form()

 
    return render (request, 'GAIA_ME_CORECTIVA_TEMPLATES/RAPORT_SUBASSET_NEW_0.1.html',{'form':form, 'Raport':RaportAvarie })    


@login_required
def NewRaportSubAsset11VIEW(request,pk):

    RaportAvarie=RaportAvarieSubAsset.objects.get(pk=pk)
    current_user_name = request.user.username

    #ADDED NEW TO NOT BE ABLE TO EDIT

    if RaportAvarie.Status==1  :
        return redirect('phome' )
        

    ###########################



    if request.method=='POST':

        form=NewRaportSubAsset11Form(request.POST)
        if form.is_valid() :

            RaportAvarie.Observatii=form.cleaned_data['Observatii']
            RaportAvarie.NUME_ME_2=current_user_name
            RaportAvarie.Cod_Marca_ME_2=form.cleaned_data['Cod_Marca_ME_2']
            RaportAvarie.Status_OPEN=1
            RaportAvarie.Status=1


            RaportAvarie.save()
            return redirect('phome' )

    else:

        form=NewRaportSubAsset11Form()

 
    return render (request, 'GAIA_ME_CORECTIVA_TEMPLATES/RAPORT_SUBASSET_NEW_1.1.html',{'form':form, 'Raport':RaportAvarie })




#MAIN RAPOARTE ASSET

#RAPOARTE  -PRODUCTIE
@login_required
def me_corectiva_vezi_rapoart_asset(request,pk) :
    RaportAvarie=RaportAvarieAsset.objects.get(pk=pk)
    return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_PRODUCTIE_VEZI_RAPORT_ASSET.html',{'Raport':RaportAvarie })
    
@login_required
def me_corectiva_vezi_rapoart_subasset(request,pk):
    RaportAvarie=RaportAvarieSubAsset.objects.get(pk=pk)
    return render(request, 'GAIA_ME_CORECTIVA_TEMPLATES/ME_CORECTIVA_PRODUCTIE_VEZI_RAPORT_SUBASSET.html',{'Raport':RaportAvarie })



#RAPOARTE  - MENTENANTA

@login_required
def mnt_corectiva_vezi_mentenanta_rapoart_subasset(request,pk):
    RaportAvarie=RaportAvarieSubAsset.objects.get(pk=pk)
    return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_MENTENANTA_VEZI_RAPORT_SUBASSET.html',{'Raport':RaportAvarie })

@login_required
def mnt_corectiva_mentenanta_vezi_rapoart_asset(request,pk) :
    RaportAvarie=RaportAvarieAsset.objects.get(pk=pk)
    return render(request, 'GAIA_MNT_CORECTIVA_TEMPLATES/MNT_CORECTIVA_MENTENANTA_VEZI_RAPORT_ASSET.html',{'Raport':RaportAvarie })
