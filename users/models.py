from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from .validators import cpf_validator, date_of_birth_validator, group_validator


class UserManager(BaseUserManager):
    def create_user(self, full_name, cpf, date_of_birth, group, had_covid_last_month, password, **other_fields):

        user = self.model(
            full_name=full_name,
            cpf=cpf,
            date_of_birth=date_of_birth,
            group=group,
            had_covid_last_month=had_covid_last_month,
            **other_fields
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, full_name, cpf, date_of_birth, group, had_covid_last_month, password, **other_fields):
        other_fields.setdefault('is_superuser', True)

        # Verifiers
        if not other_fields.get('is_superuser'):
            raise ValueError(_("is_superuser deveria ter valor True"))

        return (self.create_user(full_name, cpf, date_of_birth, group, had_covid_last_month, password, **other_fields))

# GRUPOS_DE_ATENDIMENTO MODEL


class Group(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name='user')
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
    cpf = models.CharField( unique=True, null=False, max_length=11, validators=[cpf_validator])
    username = None
    date_of_birth = models.DateField(validators=[date_of_birth_validator])
    group = models.ForeignKey("users.Group", on_delete=models.CASCADE, related_name="group", null=True)
    aptitude = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['full_name', 'date_of_birth', 'group']

    

    objects = UserManager()

    def __str__(self):
        return self.cpf

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
