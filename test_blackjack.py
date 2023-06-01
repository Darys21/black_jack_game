import unittest
from blackjack import Deck, Card

class TestDeck(unittest.TestCase):
    def test_build(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

        expected_values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
        expected_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        for card in deck.cards:
            self.assertIn(card.value, expected_values)
            self.assertIn(card.suit, expected_suits)

    def test_shuffle(self):
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)

    def test_deal(self):
        deck = Deck()
        card = deck.deal()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.cards), 51)

if __name__ == '__main__':
    unittest.main()
