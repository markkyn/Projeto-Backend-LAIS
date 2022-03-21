from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.core.management.commands import loaddata

class Command(BaseCommand):
    help = 'Adiciona os estabelecimentos do arquivo estabelecimentos_pr.xml'

    def handle(self, *args, **kwargs):
        pass