# Generated by Django 3.2.9 on 2022-03-16 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ME_CORECTIVA', '0026_auto_20220316_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 215192), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 215192), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 215192), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 215192), verbose_name='Data Semnalare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 216191), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 216191), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 216191), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 16, 12, 45, 31, 216191), verbose_name='Data Semnalare Raport'),
        ),
    ]