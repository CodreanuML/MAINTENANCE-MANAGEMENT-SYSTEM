# Generated by Django 3.2.9 on 2022-02-25 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('GAIA_ACCOUNTS', '0002_employee_zona'),
        ('GAIA_ASSETS', '0011_subasset_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actiune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire', models.CharField(max_length=50, unique=True)),
                ('cauza', models.CharField(max_length=100)),
                ('Actiune', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('data_deschidre_actiune', models.DateField()),
                ('data_preconizare_finalizare', models.DateField()),
                ('data_finaliarii', models.DateField()),
                ('data_verificarii_eficientei', models.DateField()),
                ('comentarii', models.TextField(max_length=100)),
                ('responsabil', models.ManyToManyField(to='GAIA_ACCOUNTS.Employee')),
                ('zona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Zona_Actiune', to='GAIA_ASSETS.zona')),
            ],
        ),
    ]
