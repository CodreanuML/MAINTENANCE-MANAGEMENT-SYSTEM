# Generated by Django 3.2.9 on 2021-11-17 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire', models.CharField(max_length=80)),
                ('subasset_val', models.BooleanField()),
                ('data_adaugare', models.DateTimeField(auto_now_add=True)),
                ('ID_Asset', models.CharField(max_length=30, unique=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=30, unique=True)),
                ('descriere', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire', models.CharField(max_length=80)),
                ('data_adaugare', models.DateTimeField(auto_now_add=True)),
                ('ID_SubAsset', models.CharField(max_length=30, unique=True)),
                ('Asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Asset', to='GAIA_ASSETS.asset')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='Zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Zona', to='GAIA_ASSETS.zona'),
        ),
    ]