from json import JSONDecodeError
from urllib.error import URLError

from django.http import Http404
from django.shortcuts import render
from .services import get_cards


def home(request):
	try:
		cards = get_cards()
		unavailable = False
	except (URLError, TimeoutError, JSONDecodeError):
		cards = []
		unavailable = True

	return render(request, 'cards/list.html', {
		'cards': cards,
		'unavailable': unavailable,
	})


def card_detail(request, card_id):
	try:
		cards = get_cards()
	except (URLError, TimeoutError, JSONDecodeError):
		return render(request, 'cards/detail.html', {'unavailable': True}, status=503)

	card = next((item for item in cards if item['id'] == card_id), None)
	if card is None:
		raise Http404('No se encontró esa carta.')

	return render(request, 'cards/detail.html', {'card': card})
