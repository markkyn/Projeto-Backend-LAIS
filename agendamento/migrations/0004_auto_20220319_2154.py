# Generated by Django 3.1.3 on 2022-03-20 00:54

import agendamento.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0003_auto_20220319_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='appointment_date',
            field=models.DateField(validators=[agendamento.validators.previous_date_validator, agendamento.validators.weekday_validator]),
        ),
    ]
