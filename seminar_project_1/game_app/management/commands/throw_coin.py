from random import randint

from django.core.management.base import BaseCommand
from ...models import Coin


class Command(BaseCommand):
	help = "Throw a coin."
	
	def handle(self, *args, **kwargs):
		Coin.add_throws(randint(0, 1))
		
