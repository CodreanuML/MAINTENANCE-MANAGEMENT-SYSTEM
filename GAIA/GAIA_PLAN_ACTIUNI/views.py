from django.shortcuts import render
from .models import Actiune
# Create your views here.
from GAIA_ASSETS.models import Zona
from django.views.generic.edit import CreateView ,  UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import Form_add_actiune
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render , redirect, get_object_or_404  


"""ASAMBLARE"""
@login_required
def asamblare_actiuni_main(request):
	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :


		Zona1=Zona.objects.get(nume="Asamblare")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_ASAMBLARE_MAIN.html',{'page_obj':page_obj})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')


"""AIRBAG"""

@login_required
def airbag_actiuni_main(request):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		Zona1=Zona.objects.get(nume="Airbag")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_AIRBAG_MAIN.html',{'page_obj':page_obj})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')


"""DIECASTING"""
@login_required
def diecasting_actiuni_main(request):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		Zona1=Zona.objects.get(nume="Diecasting")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_DIECASTING_MAIN.html',{'page_obj':page_obj})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')

"""FOAMING"""
@login_required
def foaming_actiuni_main(request):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		Zona1=Zona.objects.get(nume="Foaming")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_FOAMING_MAIN.html',{'page_obj':page_obj})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')
"""IMO"""

@login_required
def imo_actiuni_main(request):




	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		Zona1=Zona.objects.get(nume="IMO")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_IMO_MAIN.html',{'page_obj':page_obj})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')
"""LW"""
@login_required
def lw_actiuni_main(request):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		Zona1=Zona.objects.get(nume="LW")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_LW_MAIN.html',{'page_obj':page_obj})
	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')


"""TOOLSHOP"""
@login_required
def toolshop_actiuni_main(request):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		Zona1=Zona.objects.get(nume="Toolshop")
		queryset=Actiune.objects.filter(zona=Zona1)

		page = request.GET.get('page', 1)
		paginator = Paginator(queryset, 10)
		try:
			page_obj = paginator.page(page)
		except PageNotAnInteger:
        # fallback to the first page
			page_obj = paginator.page(1)
		except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
			page_obj= paginator.page(paginator.num_pages)
		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_TOOLSHOP_MAIN.html',{'page_obj':page_obj})
	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')



#class add_actiune(LoginRequiredMixin,CreateView):
#	model=Actiune
#	fields=['denumire','cauza','Actiune','responsabil','status','data_deschidre_actiune','data_preconizare_finalizare','comentarii','zona']
#	template_name='GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_ADD_ACTIUNE.html'
#	success_url=reverse_lazy('GAIA_PLAN_ACTIUNI:asamblare_actiuni_main')


@login_required
def add_actiune(request):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		if request.method=='POST':
			form=Form_add_actiune(request.POST)
			if form.is_valid():
				Actiune=form.save(commit=False)
				Actiune.save()
				return redirect('GAIA_PLAN_ACTIUNI:asamblare_actiuni_main')

		else :
			form=Form_add_actiune()

		return render(request,'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_ADD_ACTIUNE.html',{'form':form})

	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')



@login_required
def vizualizare_actiune(request,pk):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :
		queryset=Actiune.objects.get(pk=pk)


		return render(request, 'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_VEZI_DETALII_PLAN.html' , {'Actiune':queryset})
	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')



#class editeaza_actiune(LoginRequiredMixin,UpdateView):
#	model=Actiune
#	fields=['cauza','Actiune','responsabil','status','data_finaliarii','data_verificarii_eficientei','comentarii']
#	template_name='GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_EDITARE_ACTIUNE.html'
#	success_url=reverse_lazy('GAIA_PLAN_ACTIUNI:asamblare_actiuni_main')	




@login_required
def editeaza_actiune(request,pk):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin' :

		actiune_req=Actiune.objects.get(pk=pk)
		form=Form_add_actiune(instance=actiune_req)


		if request.method=='POST':
			form=Form_add_actiune(request.POST,instance=actiune_req)
			if form.is_valid():
				form.save()
				return redirect('GAIA_PLAN_ACTIUNI:asamblare_actiuni_main')

		else:
			form=Form_add_actiune(instance=actiune_req)


		return render(request,'GAIA_PLAN_ACTIUNI/PLAN_ACTIUNI_EDITARE_ACTIUNE.html',{'form':form})


	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')