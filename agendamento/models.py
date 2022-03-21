from django.db import models
from .validators import previous_date_validator, time_validator, weekday_validator
import datetime as dt

from core import settings

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=255)
    cnes = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.nome} ( {self.cnes} )"

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank = True,
    )
    
    appointment_date = models.DateField(validators= [previous_date_validator, weekday_validator])
    appointment_hour = models.TimeField(validators= [time_validator])

    is_active = models.BooleanField(default=True)
    
    @property
    def quantidade_vagas(self):
        appointment = self.objects.get(id = self.id)
        return appointment.users.all().count()
    
    @property
    def is_expired(self):
        if dt.date.today() > self.appointment_date \
        or ( dt.date.today() == self.appointment_date \
             and dt.datetime.now().time() > ( self.appointment_hour )
           ):
            return True
        return False

    @property
    def weekday(self):
        days = ['Segunda', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        return "{:2}".format(days[dt.date.weekday(self.appointment_date)])
    
    @property
    def estabelecimento_formated(self):
        return f"{ self.estabelecimento.cnes} - {self.estabelecimento.nome}"

    def __str__(self):
        return f"{self.weekday} , {self.appointment_date} ({self.appointment_hour})"
    