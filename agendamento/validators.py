# DATE VALIDATORS
from datetime import date, time as dtTime
import time


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def previous_date_validator(appointment_date):
    if date.today() > appointment_date:
        raise ValidationError("Datas anteriores não são aceitas para agendamento")

def weekday_validator(appointment_date):
    week_day = appointment_date.weekday()
    print(week_day)
    # Quarta-Feira = 2
    # Sabado = 5
    if week_day > 5 \
    or week_day < 2:
        raise ValidationError("O Agendamento está disponível entre quarta-feira e sexta-feira ")

def time_validator(value):
    if value < dtTime(13) or value >= dtTime(18):
        raise ValidationError("O Agendamento só pode ser feito nos horários entre 13:00 e 17:59 horas")