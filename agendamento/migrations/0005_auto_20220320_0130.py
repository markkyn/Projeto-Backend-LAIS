# Generated by Django 3.1.3 on 2022-03-20 04:30

import agendamento.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0004_auto_20220319_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='appointment_hour',
            field=models.TimeField(validators=[agendamento.validators.time_validator]),
        ),
    ]
