from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from users.models import User

def cpf_already_registered(cpf):
    if User.objects.filter(cpf = cpf).exists():
        raise ValidationError(
            _("%(value)s Idade Inválida ( menores de 18 anos não são aceitos )"),
            params ={'value', cpf}
        )
    return False
    