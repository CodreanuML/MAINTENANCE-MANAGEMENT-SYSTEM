# Generated by Django 3.2.9 on 2022-02-10 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ME_CORECTIVA', '0011_auto_20220129_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 712623), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 712623), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 712623), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 712623), verbose_name='Data Semnalare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 713621), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 713621), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 713621), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 10, 12, 31, 12, 713621), verbose_name='Data Semnalare Raport'),
        ),
    ]
