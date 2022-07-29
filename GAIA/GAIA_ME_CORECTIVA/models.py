from django.db import models
from GAIA_ASSETS.models import Zona,Asset,SubAsset,AvarieAsset
from datetime import datetime
# Create your models here.



class RaportAvarieAsset(models.Model) :
    numar=models.IntegerField(default=0,verbose_name = 'Numarul Raportului') # """ NUMARUL RAPORTULUI """
    denumire=models.CharField(max_length=50,default='empty',verbose_name = 'Denumirea Raportului' ) # """ DENUMIRE RAPORTULUI """
    descriere=models.CharField(max_length=80,default='empty',verbose_name = 'Descrierea Raportului') # """ DESCRIEREA RAPORTULUI  """
    cauza_avariei=models.ForeignKey(AvarieAsset,related_name='Avarie_raport',on_delete=models.CASCADE, blank=True, null=True) # """ CAUZA AVARIEI   """
    activitati_efectuate=models.CharField(max_length=80 , default='empty',verbose_name = 'Activitati Efectuate') # """ ACTIVITATI EFECTUATE  """
    Asset=models.ForeignKey(Asset, related_name='Asset_Raport', on_delete=models.CASCADE,verbose_name = 'Asset') # """ ASETUL DE CARE FACE PARTE """
    Status=models.BooleanField(verbose_name = 'Status INCHIS/DESCHIS') # """ STATUSUL 0 -OPEN , 1 - CLOSED """
    Status_OPEN=models.BooleanField(verbose_name = 'Status ME/MNT') # """ STATUSUL 0 -ME , 1 - MNT """
    Status_Preluat_MNT=models.BooleanField(default=0,verbose_name = 'Preluat NE/Preluat') # """ STATUSUL 0 -NE Preluat , 1 - Preluat """
    Observatii=models.CharField(max_length=80, default='empty',verbose_name = 'Observatii') # """ OBSERVATII AVARIEI   """

    NUME_MAINT=models.CharField(max_length=80 , default='empty',verbose_name = 'Nume Tehnician Mentenanta') # """ NUMELE CELUI CARE A INCHIS RAPORTUL   """
    Cod_Marca_MAINT=models.IntegerField(default=0,verbose_name = 'Cod Marca Tehnician Mentenanta') # """ CODUL DE MARCA A CELUI CARE INCHIS RAPORTUL   """

    NUME_ME_1=models.CharField(max_length=80, default='empty',verbose_name = 'Nume Initiator Raport Avarie') # """ NUMELE CELUI CARE A DESCHIS RAPORTUL   """
    Cod_Marca_ME_1=models.IntegerField(default=0,verbose_name = 'Cod Marca Initiator Raport Avarie') # """ CODUL DE MARCA A CELUI CARE DESCIDE RAPORTUL   """

    NUME_ME_2=models.CharField(max_length=80 , default='empty',verbose_name = 'Numele Persoanei Aprobare Inchidere Avarie') # """ NUMELE CELUI CARE A INCHIS RAPORTUL   """
    Cod_Marca_ME_2=models.IntegerField(default=0,verbose_name = 'Cod Marca Persoanei Aprobare Inchidere Avarie') # """ CODUL DE MARCA A CELUI CARE A INCHIS RAPORTUL   """


    Semnalat_de_productie = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Semnalare Raport')  # """ Data si ora la care a fost semnalizata """
    Comunicat_la_intretinere = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Comunicare Raport')  # """ Data si ora la care a fost Anuntata mentenanta """
    Interventie_inceputa = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Preluare Raport')  # """ Data la care a fost inceputa interventia """
    Interventie_finalizata = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Finalizare Raport') # """ Data la care a fost finalizata interventia """


    durata_interventie=models.IntegerField(default=0,verbose_name = 'Durata Interventie') # Durata interventiei 
    durata_interventie_totala=models.IntegerField(default=0)

    total_subassets=models.IntegerField(default=0)


    def __str__(self):
        return self.denumire



class RaportAvarieSubAsset(models.Model) :
    numar=models.IntegerField(default=0,verbose_name = 'Numarul Raportului') # """ NUMARUL RAPORTULUI """
    denumire=models.CharField(max_length=50,default='empty',verbose_name = 'Denumirea Raportului' ) # """ DENUMIRE RAPORTULUI """
    descriere=models.CharField(max_length=80,default='empty',verbose_name = 'Descrierea Raportului') # """ DESCRIEREA RAPORTULUI  """
    cauza_avariei=models.ForeignKey(AvarieAsset,related_name='Avarie_raport_Sub',on_delete=models.CASCADE, blank=True, null=True) # """ CAUZA AVARIEI   """
    activitati_efectuate=models.CharField(max_length=80 , default='empty',verbose_name = 'Activitati Efectuate') # """ ACTIVITATI EFECTUATE  """
    Asset=models.ForeignKey(Asset, related_name='Asset_Raport_Sub', on_delete=models.CASCADE,verbose_name = 'Asset_Sub') # """ ASETUL DE CARE FACE PARTE """
    SubAsset=models.ForeignKey(SubAsset, related_name='Sub_Asset_Raport_Sub', on_delete=models.CASCADE,verbose_name = 'SubAsset_Sub') # """ SubASETUL DE CARE FACE PARTE """
    Status=models.BooleanField(verbose_name = 'Status INCHIS/DESCHIS') # """ STATUSUL 0 -OPEN , 1 - CLOSED """
    Status_OPEN=models.BooleanField(verbose_name = 'Status ME/MNT') # """ STATUSUL 0 -ME , 1 - MNT """
    Status_Preluat_MNT=models.BooleanField(default=0,verbose_name = 'Preluat NE/Preluat') # """ STATUSUL 0 -NE Preluat , 1 - Preluat """
    Observatii=models.CharField(max_length=80, default='empty',verbose_name = 'Observatii') # """ OBSERVATII AVARIEI   """

    NUME_MAINT=models.CharField(max_length=80 , default='empty',verbose_name = 'Nume Tehnician Mentenanta') # """ NUMELE CELUI CARE A INCHIS RAPORTUL   """
    Cod_Marca_MAINT=models.IntegerField(default=0,verbose_name = 'Cod Marca Tehnician Mentenanta') # """ CODUL DE MARCA A CELUI CARE INCHIS RAPORTUL   """

    NUME_ME_1=models.CharField(max_length=80, default='empty',verbose_name = 'Nume Initiator Raport Avarie') # """ NUMELE CELUI CARE A DESCHIS RAPORTUL   """
    Cod_Marca_ME_1=models.IntegerField(default=0,verbose_name = 'Cod Marca Initiator Raport Avarie') # """ CODUL DE MARCA A CELUI CARE DESCIDE RAPORTUL   """

    NUME_ME_2=models.CharField(max_length=80 , default='empty',verbose_name = 'Numele Persoanei Aprobare Inchidere Avarie') # """ NUMELE CELUI CARE A INCHIS RAPORTUL   """
    Cod_Marca_ME_2=models.IntegerField(default=0,verbose_name = 'Cod Marca Persoanei Aprobare Inchidere Avarie') # """ CODUL DE MARCA A CELUI CARE A INCHIS RAPORTUL   """


    Semnalat_de_productie = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Semnalare Raport')  # """ Data si ora la care a fost semnalizata """
    Comunicat_la_intretinere = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Comunicare Raport')  # """ Data si ora la care a fost Anuntata mentenanta """
    Interventie_inceputa = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Preluare Raport')  # """ Data la care a fost inceputa interventia """
    Interventie_finalizata = models.DateTimeField(default=datetime.now(),verbose_name = 'Data Finalizare Raport') # """ Data la care a fost finalizata interventia """


    durata_interventie=models.IntegerField(default=0,verbose_name = 'Durata Interventie') # Durata interventiei 



    def __str__(self):
        return self.denumire
