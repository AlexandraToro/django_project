from django.core.management.base import BaseCommand
from ...models import Coin


class Command(BaseCommand):
	help = "Throw a coin."
	
	def add_arguments(self, parser):
		parser.add_argument('amount', type=int, help='Amount of last throws')
	
	def handle(self, *args, **kwargs):
		amount = kwargs.get('amount')
		res= str(Coin.get_throws(amount))
		self.stdout.write(res)
