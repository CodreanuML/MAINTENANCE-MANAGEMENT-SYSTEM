# Generated by Django 3.2.9 on 2021-12-15 08:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ASSETS', '0010_auto_20211215_0843'),
        ('GAIA_ME_CORECTIVA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 10, 44, 36, 152279), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 10, 44, 36, 152279), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 10, 44, 36, 152279), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 10, 44, 36, 152279), verbose_name='Data Semnalare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='cauza_avariei',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Avarie_raport', to='GAIA_ASSETS.asset'),
        ),
    ]
