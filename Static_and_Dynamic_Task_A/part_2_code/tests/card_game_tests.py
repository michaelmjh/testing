import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    

    def setUp(self):
        self.card_game_1 = CardGame()
        self.card_1 = Card("spade", 1)
        self.card_2 = Card("club", 2)
        self.cards = [self.card_1, self.card_2]

    
    def test_check_for_ace_true(self):
        self.assertTrue(self.card_game_1.check_for_ace(self.card_1))

    
    def test_check_for_ace_false(self):
        self.assertFalse(self.card_game_1.check_for_ace(self.card_2))

    
    def test_highest_card(self):
        self.assertEqual(self.card_2, self.card_game_1.highest_card(self.card_1, self.card_2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 3", self.card_game_1.cards_total(self.cards))