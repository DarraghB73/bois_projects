import random

#Class for individual cards
class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        if self.value == "Joker":
            return "Joker"
        else:
            return f"{self.value} of {self.suit}"
    
#Class for a deck of cards
class Deck:
    def __init__(self, jokers = 0) -> None:
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        #create 52 cards and adds them to self.cards
        self.cards = [Card(suit, value) for suit in suits for value in values]

        #if jokers are requested, add the quantity requested
        if jokers != 0:
            for i in range(jokers):
                self.cards.append(Card("Joker", "Joker"))

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