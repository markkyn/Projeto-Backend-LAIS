from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from datetime import date
import re

# GROUP VALIDATION
# TODO: implement this
def group_validator(value):
    pass

# CPF VALIDATION
def cpf_validator(value):
    cpf_clean = re.sub('\D', '', value)

    if not is_valid_cpf(cpf_clean):
        raise ValidationError(
            _(" %(value)s é um CPF Inválido "),
            params={'value': value}
        )


def is_valid_cpf(cpf):  # Only Numbers
    known_invalid_cpfs = [
        "00000000000" == cpf,
        "11111111111" == cpf,
        "22222222222" == cpf,
        "33333333333" == cpf,
        "44444444444" == cpf,
        "55555555555" == cpf,
        "66666666666" == cpf,
        "77777777777" == cpf,
        "88888888888" == cpf,
        "99999999999" == cpf
    ]

    if(len(cpf) == 11 and cpf.isnumeric() and not any(known_invalid_cpfs)):

        # Verificacao do Primeiro Digito
        aux = 0  # Soma dos Digitos
        for i in range(len(cpf) - 2):
            aux += int(cpf[i]) * (10 - i)

        if((aux * 10) % 11 != int(cpf[9])):
            return False

        # Verificacao do Segundo Digito
        aux = 0
        for i in range(len(cpf) - 1):
            aux += int(cpf[i]) * (11 - i)

        if ((aux * 10) % 11 != int(cpf[10])):
            return False

        return True

    else:
        return False

# Date of Birth VALIDATION
def date_of_birth_validator(value):
    if age(value,date.today()) < 18:
        raise ValidationError(
            _("%(value)s Idade Inválida ( menores de 18 anos não são aceitos )"),
            params ={'value', value}
        )


def age(date_of_birth, today):
    return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))