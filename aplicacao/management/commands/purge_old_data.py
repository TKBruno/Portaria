from django.core.management.base import BaseCommand, CommandError
from aplicacao.models import Visitante 
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Excluir visitantes a cada 30 dias'

    def handle(self, *args, **options):
        Visitante.objects.filter(hora_entrada__lte=datetime.now()-timedelta(days=30)).delete()
        self.stdout.write('Excluído visitantes a cada 30 dias')