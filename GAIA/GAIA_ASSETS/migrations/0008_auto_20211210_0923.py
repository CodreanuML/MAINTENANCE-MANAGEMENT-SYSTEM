# Generated by Django 3.2.9 on 2021-12-10 07:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ASSETS', '0007_auto_20211206_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Comunicat_la_intretinere',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 9, 23, 6, 779180), verbose_name='Data Comunicare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_finalizata',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 9, 23, 6, 779180), verbose_name='Data Finalizare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Interventie_inceputa',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 9, 23, 6, 779180), verbose_name='Data Preluare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='Semnalat_de_productie',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 9, 23, 6, 779180), verbose_name='Data Semnalare Raport'),
        ),
        migrations.AlterField(
            model_name='raportavarieasset',
            name='cauza_avariei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Avarie_raport', to='GAIA_ASSETS.asset'),
        ),
        migrations.CreateModel(
            name='AvarieAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire', models.CharField(max_length=50)),
                ('Asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asset_avarie', to='GAIA_ASSETS.asset')),
            ],
        ),
    ]
