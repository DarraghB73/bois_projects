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
        cards = [str(self.cards[n]) for n in range(len(self.cards))]
        return ", ".join(cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_one(self) -> Card:
        return self.cards.pop(0)
    
    def deal_hand(self, hand_size: int) -> list:
        hand = [self.cards.pop(0) for i in range(hand_size)]        
        return hand