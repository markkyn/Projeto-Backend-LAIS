from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User

def cpf_already_registered(cpf):
    if User.objects.filter(cpf = cpf).exists():
        raise ValidationError(
            _("Já existe um cadastro com esse CPF")
        )
    return False
    