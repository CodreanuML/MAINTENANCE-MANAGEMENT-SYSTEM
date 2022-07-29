from django import forms
from .models import Actiune


class Form_add_actiune(forms.ModelForm):

	class Meta:
		model=Actiune
		fields=['denumire','cauza','Actiune','responsabil','status','data_deschidre_actiune','data_preconizare_finalizare','data_finaliarii','data_verificarii_eficientei','comentarii','zona']
		labels=['Denumire actiune','Cauza actiunii','Descrirea actiunii','Responsabili','Statusul actiunii','Data deschidere actiune','Data preconizare finalizare','Comentarii','Zona']