from django.contrib.auth import login 
from django.shortcuts import render, redirect
from .forms import LoginForm , RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from GAIA_ASSETS.models import Zona
from .models import Employee
from django.http import HttpResponse , request


from GAIA_ME_CORECTIVA.models import RaportAvarieAsset,RaportAvarieSubAsset

from django.contrib import messages


#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            login(request, user)
#            return redirect('assets_airbag_main')
#    else:
#        form = SignUpForm()
#    return render(request, 'ACCOUNTS_REGISTER.html', {'form': form})




def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            messages.success(request,f'Autentificare reusita')
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            login(request, user)
            return redirect('GAIA_ACCOUNTS/home.html')
    else:
        form = LoginForm()
    return render(request, 'GAIA_ACCOUNTS/ACCOUNTS_LOGIN.html', {'form': form})

@login_required
def home(request):

    return render(request, 'GAIA_ACCOUNTS/home.html')




@login_required

def main(request):
    current_user=request.user.employee
    current_user_department = request.user.employee.department
    current_user_zona = request.user.employee.Zona

    Zona_q=Zona.objects.get(nume=current_user_zona)






    if current_user_department == 'Mentenanta' :
        Rapoarte_asset_de_preluat=RaportAvarieAsset.objects.filter(Status_OPEN=0)
        Rapoarte_subasset_de_preluat=RaportAvarieSubAsset.objects.filter(Status_OPEN=0)

        return render(request,'GAIA_ACCOUNTS/USER_MAINT_MAIN_VIEW.html',{'Raport_asset':Rapoarte_asset_de_preluat,'Raport_subasset':Rapoarte_subasset_de_preluat})

    if current_user_department == 'Productie' :

        Rapoarte_asset_de_preluat=RaportAvarieAsset.objects.filter(Status=0,Status_OPEN=1,Asset__Zona=Zona_q)
        Rapoarte_subasset_de_preluat=RaportAvarieSubAsset.objects.filter(Status=0,Status_OPEN=1,Asset__Zona=Zona_q)

        return render(request,'GAIA_ACCOUNTS/USER_ME_MAIN_VIEW.html',{'Raport_asset':Rapoarte_asset_de_preluat,'Raport_subasset':Rapoarte_subasset_de_preluat,'Zona':Zona_q})



@login_required


def creare_utilizator_me(request):
    current_user_department = request.user.employee.department
      
    if current_user_department == 'Admin' :

        if request.method == 'POST':

            form=RegistrationForm(request.POST)
            if form.is_valid():
                user1=form.save(commit=True)
                user_name=form.cleaned_data['username']
                user1.save()
                employee_department=form.cleaned_data['department']
                employee_Zona=form.cleaned_data['Zona']
                Employee_enq=Employee.objects.create(user=user1,department=employee_department,Zona=employee_Zona)
                Employee_enq.save()
               
                messages.success(request,'Inregistrare utilizator cu success : ' +str(user_name) )

            else:
                messages.success(request,'Utilizatorul nu a fost inregistrat, a aparut o eroare.Verificati Numele si Parola.' )

            return redirect('home')

            
        else : 

            form=RegistrationForm()
        return render(request,'GAIA_ACCOUNTS/USER_ADMIN_ME_MAIN_VIEW.html',{'form':RegistrationForm})



    else : 

        return render(request, 'GAIA_ACCOUNTS/home.html')


@login_required


def creare_utilizator_mnt(request):
    current_user_department = request.user.employee.department
      
    if current_user_department == 'Admin' :

        if request.method == 'POST':

            form=RegistrationForm(request.POST)
            if form.is_valid():
                user1=form.save(commit=True)
                user_name=form.cleaned_data['username']
                user1.save()
                employee_department=form.cleaned_data['department']
                employee_Zona=form.cleaned_data['Zona']
                Employee_enq=Employee.objects.create(user=user1,department=employee_department,Zona=employee_Zona)
                Employee_enq.save()
               
                messages.success(request,'Inregistrare utilizator cu success : ' +str(user_name) )

            else:
                messages.success(request,'Utilizatorul nu a fost inregistrat, a aparut o eroare.Verificati Numele si Parola.' )

            return redirect('home')

            
        else : 

            form=RegistrationForm()
        return render(request,'GAIA_ACCOUNTS/USER_ADMIN_MNT_MAIN_VIEW.html',{'form':RegistrationForm})



    else : 

        return render(request, 'GAIA_ACCOUNTS/home.html')


