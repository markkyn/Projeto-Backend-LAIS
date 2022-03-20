from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models import Q
from .validators import cpf_validator, age_validator, group_validator

from datetime import date

class UserManager(BaseUserManager):
    def create_user(self, full_name, cpf, date_of_birth, password, **other_fields):

        user = self.model(
            full_name=full_name,
            cpf=cpf,
            date_of_birth=date_of_birth,
            **other_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, full_name, cpf, date_of_birth, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('had_covid_last_month', False)

        # Verifiers
        if not other_fields.get('is_superuser'):
            raise ValueError(_("is_superuser deveria ter valor True"))

        return (self.create_user(full_name, cpf, date_of_birth, password, **other_fields))

# GRUPOS_DE_ATENDIMENTO MODEL
class Group(models.Model):
    nome = models.CharField(max_length=255)
    visivel = models.BooleanField(default=True)
    fase = models.IntegerField(null=True, blank = True)
    grupo_pai =  models.CharField(max_length=255, null = True, blank=True)

    codigo_si_pni = models.CharField(max_length=255, null = True, blank=True)
    criado_em = models.DateTimeField()
    atualizado_em = models.DateTimeField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Grupo de Atendimento"
        verbose_name_plural = "Grupos de Atendimento"


class User(AbstractBaseUser, PermissionsMixin):
    
    
    cpf = models.CharField(
        verbose_name = "CPF",
        max_length=11,
        unique=True,
        null=False,
        validators= [ cpf_validator ]
    )
    
    full_name = models.CharField(
        verbose_name= "Nome Completo",
        max_length=255,
        blank=True
    )

    date_of_birth = models.DateField(
        verbose_name = "Data de Nascimento",
        null=True,
        validators=[ age_validator ]
    )

    had_covid_last_month = models.BooleanField(
        verbose_name = "Teve Covid nos 30 dias anteriores ao cadastro?",
        default=False,
        null=True
    )

    groups = models.ManyToManyField(
        Group, 
        related_name="groups",
        blank=True
    )
    
    username = None

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Used by Admin.site.register (Admin Panel)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['full_name', 'date_of_birth']

    def get_idade(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
    def is_able_to_schedule(self):
        return ( 
            self.get_idade() >= 18
            and not self.had_covid_last_month 
            and not self.groups.filter( Q(nome = "População Privada de Liberdade") 
                                      | Q(nome = "Pessoas ACAMADAS de 80 anos ou mais")
                                      | Q(nome = "Pessoas com Deficiência Institucionalizadas")
                                      ).exists()
        )
    
    def __str__(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[-2:]}'
    
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
