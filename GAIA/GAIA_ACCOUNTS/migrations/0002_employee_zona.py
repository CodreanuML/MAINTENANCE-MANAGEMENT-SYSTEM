# Generated by Django 3.2.9 on 2022-01-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_ACCOUNTS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Zona',
            field=models.CharField(default='empty', max_length=100),
        ),
    ]