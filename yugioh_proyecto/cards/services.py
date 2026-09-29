import json
from urllib.request import Request, urlopen

from django.core.cache import cache


API_URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Blue-Eyes'
CACHE_KEY = 'blue_eyes_cards'


def get_cards():
	cards = cache.get(CACHE_KEY)
	if cards is not None:
		return cards

	request = Request(API_URL, headers={'User-Agent': 'BlueEyesArchive/1.0'})
	with urlopen(request, timeout=12) as response:
		cards = json.loads(response.read().decode('utf-8')).get('data', [])
	cache.set(CACHE_KEY, cards, 60 * 15)
	return cards