from django.core.management.base import BaseCommand
from ...models import Client


class Command(BaseCommand):
	help = "update client by ID"
	
	def add_arguments(self, parser):
		parser.add_argument('pk', type=int, help='ID of client')
		parser.add_argument('email', type=str, help='New email')
	
	def handle(self, *args, **kwargs):
		pk = kwargs.get('pk')
		email = kwargs.get('email')
		client = Client.objects.filter(pk=pk).first()
		if client:
			client.email = email
			client.save()
		self.stdout.write(f'Update data: {client}, new email {client.email}')
