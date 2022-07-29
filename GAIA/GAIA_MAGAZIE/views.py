from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView ,UpdateView
from .models import Location,Item
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
# Create your views here.
from .forms import Form_add_location , Form_add_item
from django.contrib.auth.decorators import login_required
#class main_locatii(ListView):
#	model=Location
#	template_name='GAIA_MAGAZIE/GAIA_MAGAZIE_MAIN_LOCATII.html'
#	paginate_by = 10


@login_required
def main_locatii(request):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':

		queryset=Location.objects.all()
		page=request.GET.get('page',1)
		paginator=Paginator(queryset,10)
		try:
			page_obj=paginator.page(page)
		except PageNotAnInteger:
			page_obj=paginator.page(1)
		except EmptyPage:
			page_obj=paginator.page(paginator.num_pages)
		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_MAIN_LOCATII.html',{'page_obj':page_obj})
	else :

		return render(request, 'GAIA_ACCOUNTS/home.html')
 
#class add_location(CreateView):
#	model=Location
#	fields=['nume']
#	template_name='GAIA_MAGAZIE/GAIA_MAGAZIE_ADD_LOCATION.html'
#	success_url=reverse_lazy('GAIA_MAGAZIE:magazie_main_locatii')

@login_required
def add_location(request):
	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':
		if request.method=='POST' :
			form=Form_add_location(request.POST)
			if form.is_valid():
				form.save()
				return redirect('GAIA_MAGAZIE:magazie_main_locatii')

		else :
			form=Form_add_location()


		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_ADD_LOCATION.html',{'form':form})
	
	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')

"""class main_items(ListView):
	model=Item
	template_name='GAIA_MAGAZIE/GAIA_MAGAZIE_MAIN_ITEMS.html'
	paginate_by = 10"""

@login_required
def main_items(request):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':
	
		queryset=Item.objects.all()	

		if 'searched' in request.GET:
			searched=request.GET['searched']
			if searched=='':
				queryset=queryset=Item.objects.all()	
			else :

				queryset=Item.objects.filter(nume__contains=searched)



		if 'searched_cod' in request.GET:
			searched=request.GET['searched_cod']
			if searched=='':
				queryset=queryset=Item.objects.all()	
			else:
				queryset=Item.objects.filter(part_no__contains=searched)


	

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


		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_MAIN_ITEMS.html',{'page_obj':page_obj} )


	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')	





#class add_item(CreateView):
#	model=Item
#	fields=['nume','part_no','location','stock_qty','unit_price','minimun_stock_qty','maximum_stock_qty','critical']
#	template_name='GAIA_MAGAZIE/GAIA_MAGAZIE_ADD_ITEM.html'
#	success_url=reverse_lazy('GAIA_MAGAZIE:magazie_main_items')

@login_required
def add_item(request):


	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':

		if request.method=='POST':

			form=Form_add_item(request.POST)

			if form.is_valid():

				form.save()

				return redirect('GAIA_MAGAZIE:magazie_main_items')
		else :

			form=Form_add_item()

		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_ADD_ITEM.html',{'form':form} )	
	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')	

""" TREBUIE MODIFICAT CU GCBV"""


@login_required
def vezi_continut_locatie(request,pk):
	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':

		locatie=Location.objects.get(pk=pk)
		queryset=Item.objects.filter(location__pk=pk)
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

		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_VEZI_DETALII_LOCATIE.html',{'locatie':locatie , 'page_obj':page_obj})
	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def item_modify_plus(request,pk):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':


		Item_q=Item.objects.get(pk=pk)
		stock_qty_1=Item_q.stock_qty

		stock_qty_1+=1 
		Item_q.stock_qty=stock_qty_1
		Item_q.save()
		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_VEZI_DETALII_ITEM.html',{'Item':Item_q} )

	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required
def item_modify_minus(request,pk):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':

		Item_q=Item.objects.get(pk=pk)
		stock_qty_1=Item_q.stock_qty
		if stock_qty_1 != 0 :
			stock_qty_1-=1 
		Item_q.stock_qty=stock_qty_1
		Item_q.save()
		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_VEZI_DETALII_ITEM.html',{'Item':Item_q} )
	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required
def vezi_detalii_obiect(request,pk):

	current_user_department = request.user.employee.department

	if current_user_department == 'Mentenanta' or current_user_department == 'Admin':


		Item_enq=Item.objects.get(pk=pk)

		return render(request,'GAIA_MAGAZIE/GAIA_MAGAZIE_VEZI_DETALII_ITEM.html',{'Item':Item_enq})


	else :
		return render(request, 'GAIA_ACCOUNTS/home.html')





	
