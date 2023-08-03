from random import randint

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def coin(request):
	side = ['avers', 'reverse'][randint(0, 1)]
	logger.info(f"coin is done, {side}")
	return HttpResponse(f"Coin side: {side}")


def dice(request):
	cube_dice = randint(1, 6)
	logger.info(f"cibe is done: {cube_dice}")
	return HttpResponse(f"Cube side: {cube_dice}")


def rand_int(request):
	rand_int = randint(0,100)
	logger.info(f"rasndom is done, {rand_int}")
	return HttpResponse(f"Random integer: {rand_int}")
