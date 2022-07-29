# Generated by Django 3.2.9 on 2021-12-02 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ASSETS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaportAvarieAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar', models.IntegerField()),
                ('denumire', models.CharField(max_length=50)),
                ('descriere', models.CharField(max_length=80)),
                ('cauza_avariei', models.CharField(max_length=80)),
                ('activitati_efectuate', models.CharField(max_length=80)),
                ('Status', models.BooleanField()),
                ('Status_OPEN', models.BooleanField()),
                ('Observatii', models.CharField(max_length=80)),
                ('NUME_MAINT', models.CharField(max_length=80)),
                ('Cod_Marca_MAINT', models.IntegerField()),
                ('NUME_ME_1', models.CharField(max_length=80)),
                ('Cod_Marca_ME_1', models.IntegerField()),
                ('NUME_ME_2', models.CharField(max_length=80)),
                ('Cod_Marca_ME_2', models.IntegerField()),
                ('Semnalat_de_productie', models.DateTimeField()),
                ('Comunicat_la_intretinere', models.DateTimeField()),
                ('Interventie_inceputa', models.DateTimeField()),
                ('Interventie_finalizata', models.DateTimeField()),
                ('durata_interventie', models.TimeField()),
                ('Asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asset_Raport', to='GAIA_ASSETS.asset')),
            ],
        ),
    ]
