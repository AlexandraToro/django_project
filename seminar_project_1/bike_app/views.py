from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
	logger.info("Visited page: index(bike)")
	return render(request, 'bike_app/index.html')


def type_of_bike(request):
	logger.info("Visited page: type of bike")
	return render(request, 'bike_app/type.html')
