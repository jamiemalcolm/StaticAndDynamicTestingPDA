import unittest
from src.card.py import Card
from src.card_game.py import CardGame

# from part_2_code.src.card import Card
# from part_2_code.src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Clubs", 2)
        self.card3 = Card("Clubs", 3)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_highest_card(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card2, self.card3))

    def test_Cards_total(self):
        self.assertEqual("You have a total of 6", self.card_game.cards_total(self.cards))