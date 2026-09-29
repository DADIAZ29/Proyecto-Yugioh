from django.test import TestCase
from unittest.mock import patch


class CardPagesTests(TestCase):
	card = {
		'id': 89631139,
		'name': 'Blue-Eyes White Dragon',
		'type': 'Normal Monster',
		'frameType': 'normal',
		'race': 'Dragon',
		'attribute': 'LIGHT',
		'atk': 3000,
		'def': 2500,
		'level': 8,
		'linkval': 3,
		'desc': 'This legendary dragon is a powerful engine of destruction.',
		'card_images': [{
			'image_url': 'https://example.com/card.jpg',
			'image_url_small': 'https://example.com/card-small.jpg',
		}],
		'card_prices': [{
			'tcgplayer_price': '25.00',
			'cardmarket_price': '20.00',
			'ebay_price': '18.00',
		}],
		'card_sets': [{
			'set_name': 'Legend of Blue Eyes White Dragon',
			'set_rarity': 'Ultra Rare',
		}],
	}

	@patch('cards.views.get_cards')
	def test_home_shows_card_image_name_and_price(self, get_cards):
		get_cards.return_value = [self.card]

		response = self.client.get('/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Blue-Eyes White Dragon')
		self.assertContains(response, 'https://example.com/card.jpg')
		self.assertContains(response, '$25.00')

	@patch('cards.views.get_cards')
	def test_detail_shows_card_attributes_and_prices(self, get_cards):
		get_cards.return_value = [self.card]

		response = self.client.get('/carta/89631139/')

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Normal Monster')
		self.assertContains(response, 'LIGHT')
		self.assertContains(response, '3000')
		self.assertContains(response, '2500')
		self.assertContains(response, 'Nivel')
		self.assertNotContains(response, 'Raza:')
		self.assertNotContains(response, 'LINK')
		self.assertNotContains(response, 'Ediciones')
		self.assertNotContains(response, 'Ultra Rare')
		self.assertContains(response, '$20.00')
