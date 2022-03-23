from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Adiciona os estabelecimentos'

    def handle(self, *args, **options):
        call_command('loaddata','estabelecimentos_formatado.json')