# Generated by Django 3.2.9 on 2022-02-25 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GAIA_PLAN_ACTIUNI', '0004_actiune_hide_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actiune',
            options={'ordering': ['hide_date']},
        ),
        migrations.AlterField(
            model_name='actiune',
            name='hide_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 25, 16, 18, 27, 567527)),
        ),
    ]