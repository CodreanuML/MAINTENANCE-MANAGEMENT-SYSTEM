# Generated by Django 3.2.9 on 2022-01-20 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ME_CORECTIVA', '0006_auto_20220110_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 172041), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 172041), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 172041), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 172041), verbose_name='Data Semnalare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 173038), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 173038), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 173038), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 20, 9, 11, 13, 173038), verbose_name='Data Semnalare Raport'),
        ),
    ]
