# Generated by Django 3.2.9 on 2022-02-25 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ME_CORECTIVA', '0017_auto_20220225_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 11093), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 11093), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 11093), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 11093), verbose_name='Data Semnalare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 12114), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 12114), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 12114), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavariesubasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 13, 45, 14, 12114), verbose_name='Data Semnalare Raport'),
        ),
    ]