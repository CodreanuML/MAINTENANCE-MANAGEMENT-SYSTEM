from django.shortcuts import render , redirect, get_object_or_404  
from django.http import HttpResponse , request
from .models import Zona , Asset , SubAsset  , AvarieAsset
from GAIA_ME_CORECTIVA.models  import RaportAvarieAsset ,RaportAvarieSubAsset
from .forms import NewAssetForm , NewSubAssetForm , NewAvarieForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
import pytz
from django.contrib.auth.decorators import login_required
utc=pytz.UTC



# Create your views here.



#HOME MAINTENANCE 




@login_required
def home_maintenance(request):


    current_user_department = request.user.employee.department
    
    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

        RaportAvarie_deschis_ME=RaportAvarieAsset.objects.filter(Status_OPEN=0)
        RaportAvarie_deschis_MNT=RaportAvarieAsset.objects.filter(Status_OPEN=1,Status=0)
        RaportAvarieSubAsset_deschis_ME=RaportAvarieSubAsset.objects.filter(Status_OPEN=0)
        RaportAvarieSubAsset_deschis_MNT=RaportAvarieSubAsset.objects.filter(Status_OPEN=1,Status=0)

        return render(request,'GAIA_ASSETS_TEMPLATES/MAINTENANCE_HOME.html',{'RaportAvarie_deschis_ME':RaportAvarie_deschis_ME,'RaportAvarie_deschis_MNT':RaportAvarie_deschis_MNT,'RaportAvarieSubAsset_deschis_ME':RaportAvarieSubAsset_deschis_ME,'RaportAvarieSubAsset_deschis_MNT':RaportAvarieSubAsset_deschis_MNT})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

# AIRBAG VIEWS ASSET #################################################################################################################
@login_required
def airbag_main(request):



    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_AIRBAG_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

#NEW ASSET - AIRBAG VIEW
@login_required
def NewAssetAirbagView(request) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

        Zona_provenienta=get_object_or_404(Zona, nume='Airbag' )

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_airbag_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_AIRBAG_NEWASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



#SUBASSET - AIRBAG VIEW
@login_required
def SubAssetAirbagView(request ,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_AIRBAG_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})



    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

#NEW NewSubAssetView - AIRBAG VIEW
@login_required
def NewSubAssetAirbagView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :    


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_airbag' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_AIRBAG_NEWSUBASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

#afisare avarii asset -AIRBAG
@login_required
def airbag_lista_avarii(request,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :    

        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_AIRBAG_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

#inregistrare avarie noua asset -AIRBAG
@login_required
def NewAirbagAvarieView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :    



        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_airbag_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_AIRBAG_NEW_AVARIEASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')




# ASAMBLARE VIEWS #################################################################################################################











@login_required
def asamblare_main(request):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_ASAMBLARE_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')









@login_required
def NewAssetAsamblareView(request) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

        Zona_provenienta=get_object_or_404(Zona, nume='Asamblare' )

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_asamblare_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_ASAMBLARE_NEWASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

  

@login_required
def NewSubAssetAsamblareView(request, pk) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_asamblare' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_ASAMBLARE_NEWSUBASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def SubAssetAsamblareView(request ,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :



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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_ASAMBLARE_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


#afisare avarii asset -ASAMBLARE
@login_required
def asamblare_lista_avarii(request,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_ASAMBLARE_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')

#inregistrare avarie noua asset -ASAMBLARE
@login_required
def NewAsamblareAvarieView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :    

        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_asamblare_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_ASAMBLARE_NEW_AVARIEASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


# DIECASTING VIEWS #################################################################################################################
@login_required
def diecasting_main(request):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :    


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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_DIECASTING_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def NewAssetDiecastingView(request) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :    

        Zona_provenienta=Zona.objects.get(nume='Diecasting')

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_diecasting_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_DIECASTING_NEWASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


  

@login_required
def NewSubAssetDiecastingView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :        

        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_diecasting' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_DIECASTING_NEWSUBASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def SubAssetDiecastingView(request ,pk):


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :        


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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_DIECASTING_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



#afisare avarii asset - DC
@login_required
def diecasting_lista_avarii(request,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :        


        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_DIECASTING_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



#inregistrare avarie noua asset -DC
@login_required
def NewDiecastingAvarieView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :      


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_diecasting_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_DIECASTING_NEW_AVARIEASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')



# FOAMING VIEWS #################################################################################################################
@login_required
def foaming_main(request):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :      

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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_FOAMING_MAIN.html',{'Assets':Assets})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def NewAssetFoamingView(request) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :      



        Zona_provenienta=get_object_or_404(Zona, nume='Foaming' )

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_foaming_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_FOAMING_NEWASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')
  



@login_required
def NewSubAssetFoamingView(request, pk) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :      


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_foaming' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_FOAMING_NEWSUBASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')    



@login_required
def SubAssetFoamingView(request ,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :  


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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_FOAMING_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')    


@login_required
def foaming_lista_avarii(request,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :  

        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_FOAMING_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')            

#inregistrare avarie noua asset -ASAMBLARE


@login_required
def NewFoamingAvarieView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :     

        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_foaming_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_FOAMING_NEW_AVARIEASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')    


# IMO VIEWS #################################################################################################################
@login_required
def imo_main(request):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_IMO_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')   


@login_required
def NewAssetImoView(request) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Zona_provenienta=get_object_or_404(Zona, nume='IMO' )

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_imo_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_IMO_NEWASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  
  





@login_required
def NewSubAssetImoView(request, pk) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_imo' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_IMO_NEWSUBASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  






@login_required
def SubAssetImoView(request ,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 



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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_IMO_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


@login_required
def imo_lista_avarii(request,pk):


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_IMO_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})



    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  







#inregistrare avarie noua asset -IMO
@login_required
def NewImoAvarieView(request, pk) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_imo_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_IMO_NEW_AVARIEASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  



# LW VIEWS #################################################################################################################
@login_required
def lw_main(request):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_LW_MAIN.html',{'Assets':Assets})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


@login_required
def NewAssetLwView(request) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Zona_provenienta=get_object_or_404(Zona, nume='LW' )

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_lw_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_LW_NEWASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  
  



@login_required
def NewSubAssetLwView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_lw' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_LW_NEWSUBASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


@login_required
def SubAssetLwView(request ,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 



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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_LW_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  

#lista avarie-LW

@login_required
def lw_lista_avarii(request,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 

        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_LW_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


#inregistrare avarie noua asset -LW
@login_required
def NewLwAvarieView(request, pk) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 

        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_lw_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_LW_NEW_AVARIEASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


# TOOLSHOP VIEWS #################################################################################################################
@login_required
def toolshop_main(request):


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


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


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_TOOLSHOP_MAIN.html',{'Assets':Assets})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


@login_required
def NewAssetToolshopView(request) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' : 


        Zona_provenienta=get_object_or_404(Zona, nume='Toolshop' )

        if request.method=='POST':

            form=NewAssetForm(request.POST)
            if form.is_valid() :

                Asset=form.save(commit=False)
                Asset.Zona=Zona_provenienta
                Asset.save()

                return redirect('assets_toolshop_main')

        else:

            form=NewAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_TOOLSHOP_NEWASSET.html',{'form':form})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  
  

@login_required
def NewSubAssetToolshopView(request, pk) :

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :     

        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewSubAssetForm(request.POST)
            if form.is_valid() :

                SubAsset=form.save(commit=False)
                SubAsset.Asset=Asset_val
                SubAsset.save()

                return redirect('subassets_toolshop' ,pk=pk)

        else:

            form=NewSubAssetForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_TOOLSHOP_NEWSUBASSET.html',{'form':form})


    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  



@login_required
def SubAssetToolshopView(request ,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :     


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
        
        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_TOOLSHOP_SUBASSET.html',{'Asset':Asset_called , 'SubAsset':SubAsset_called})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


@login_required
def toolshop_lista_avarii(request,pk):

    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :     


        Asset_requested=Asset.objects.get(pk=pk)
        queryset=AvarieAsset.objects.filter(Asset__pk=pk)
        page = request.GET.get('page', 1)
        paginator = Paginator(queryset, 10)

        try:
            Avarii = paginator.page(page)
        except PageNotAnInteger:
        # fallback to the first page
            Avarii = paginator.page(1)
        except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
            Avarii = paginator.page(paginator.num_pages)


        return render(request, 'GAIA_ASSETS_TEMPLATES/ASSETS_TOOLSHOP_LISTA_AVARII_ASSET.html',{'Avarii':Avarii,'Asset':Asset_requested})

    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  


#inregistrare avarie noua asset -Toolshop
@login_required
def NewToolshopAvarieView(request, pk) :


    current_user_department = request.user.employee.department

    if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :     


        Asset_val=Asset.objects.get(pk=pk )

        if request.method=='POST':

            form=NewAvarieForm(request.POST)
            if form.is_valid() :

                AvarieAsset=form.save(commit=False)
                AvarieAsset.Asset=Asset_val
                AvarieAsset.save()

                return redirect('assets_toolshop_lista_avarii' ,pk=pk)

        else:

            form=NewAvarieForm()

        return render (request, 'GAIA_ASSETS_TEMPLATES/ASSETS_TOOLSHOP_NEW_AVARIEASSET.html',{'form':form})
    else :

        return render(request, 'GAIA_ACCOUNTS/home.html')  