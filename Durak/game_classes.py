import random

#Class for individual cards
class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"
    
#Class for a deck of cards
class Deck:
    def __init__(self, cards: list) -> None:
        self.cards = cards

    def __str__(self) -> str:
        return_string = ''
        for card in self.cards:
            return_string += str(card) + ', '

        return return_string[:-2]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_one(self) -> Card:
        return self.cards.pop(0)
    
    def deal_hand(self, hand_size: int) -> list:
        hand = []
        for i in range(hand_size):
            hand.append(self.cards.pop(0))
        
        return hand