from django import forms
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm 
from django.contrib.auth.models import User

from .models import Employee 




class LoginForm(AuthenticationForm):
    
      class Meta:
            model = User
            fields = ('username','password')





class RegistrationForm(UserCreationForm):
    """docstring for RegistrationForm"""

    DEP_CHOICES = [
        ('Productie', 'Productie'),
        ('Mentenanta', 'Mentenanta'),
        ('Admin' , 'Admin'),

    ]


    ZONA_CHOICES = [
        ('Asamblare', 'Asamblare'),
        ('Airbag', 'Airbag'),
        ('Foaming' , 'Foaming'),
        ('Diecasting' , 'Diecasting'),
        ('LW' , 'LW'),
        ('IMO' , 'IMO'),
        ('Toolshop' , 'Toolshop'),
        ('Toate' , 'Toate'),

    ]

   
    department = forms.ChoiceField(choices=DEP_CHOICES,label='Selectati departamentul')
    Zona = forms.ChoiceField(choices=ZONA_CHOICES,label='Selectati aria')




    class Meta: # define a metadata related to this class
        model = User
        fields = (
            'username', 'password1', 'password2' ,
            'department',
            'Zona',


        )
        labels = {
 
        'department': ('Selectati departamentu'),
        'Zona': ('Selectati aria'),
        }
        
