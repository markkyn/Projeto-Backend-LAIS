from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from .validators import cpf_validator, date_of_birth_validator, group_validator


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
        other_fields.setdefault('group', None)
        other_fields.setdefault('had_covid_last_month', False)

        # Verifiers
        if not other_fields.get('is_superuser'):
            raise ValueError(_("is_superuser deveria ter valor True"))

        return (self.create_user(full_name, cpf, date_of_birth, password, **other_fields))

# GRUPOS_DE_ATENDIMENTO MODEL


class Group(models.Model):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name='user')
    grupo_pai = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    visivel = models.BooleanField(default=True)
    fase = models.IntegerField()

    codigo_si_pni = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class User(AbstractBaseUser, PermissionsMixin):
    username = None
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
        validators=[ date_of_birth_validator ]
    )

    had_covid_last_month = models.BooleanField(
        verbose_name = "Teve Covid nos 30 dias anteriores ao cadastro?",
        default=False,
        null=True
    )

    group = models.ForeignKey(
        "users.Group", 
        related_name="group",
        null=True,
        on_delete=models.CASCADE,
    )
    
    #TODO: Aptitude de ser cadastrado deve ser uma função
    aptitude = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Used by Admin.site.register (Admin Panel)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['full_name', 'date_of_birth']

    objects = UserManager()

    def __str__(self):
        return f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[-2:]}'

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
