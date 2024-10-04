import random

#Class for individual cards
class Card:
    def __init__(self, suit: str, value: str, int_value: int) -> None:
        self.suit = suit
        self.value = value
        self.int_value = int_value
        self.is_trump = False

    def __str__(self) -> str:
        if self.value == "Joker":
            return "Joker"
        else:
            return f"{self.value} of {self.suit}"
        
    def __eq__(self, second_card) -> bool:
        if self.value == second_card.value and not (self.is_trump or second_card.is_trump):
            return True
        else:
            return False
        
    def __lt__(self, second_card) -> bool:
        if self.int_value < second_card.int_value and (not self.is_trump or (self.is_trump and second_card.is_trump)):
            return True
        else:
            return False
        
    def __gt__(self, second_card) -> bool:
        if self.int_value > second_card.int_value and (self.is_trump or (not self.is_trump and not second_card.is_trump)):
            return True
        else:
            return False
        
    def set_trump(self, suit):
        if self.suit == suit:
            self.is_trump = True
    
#Class for a deck of cards
class Deck:
    def __init__(self, jokers = 0) -> None:
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        values = [("2",2), ("3",3), ("4",4), ("5",5), ("6",6), ("7",7), 
                  ("8",8), ("9",9), ("10",10), ("Jack",11), ("Queen",12), 
                  ("King",13), ("Ace",14)]

        #create 52 cards and adds them to self.cards
        self.cards = [Card(suit, value, int_value) for suit in suits 
                      for (value,int_value) in values]

        #if jokers are requested, add the quantity requested
        if jokers != 0:
            for i in range(jokers):
                self.cards.append(Card("Joker", "Joker", 15))

    def __str__(self) -> str:
        cards = [str(self.cards[n]) for n in range(len(self.cards))]
        return ", ".join(cards)
    
    def __len__(self) -> int:
        return len(self.cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal_one(self) -> Card:
        return self.cards.pop(0)
    
    def deal_hand(self, hand_size: int) -> list:
        hand = [self.cards.pop(0) for i in range(hand_size)]        
        return hand

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name
    
    def deal_hand(self, hand: list):
        self.hand = hand

class Challenge:
    def __init__(self, offense: Card, attacker: Player):
        self.offense = offense
        self.attacker = attacker
        self.defended = 0

    def __str__(self):
        string = f"{str(self.attacker)} attacks with {str(self.offense)}"
        if(self.defended == 1):
            string += f"; defended with {str(self.defense)}"
        return string

    def defend(self, defense: Card):
        if(defense > self.offense):
            self.defense = defense
            self.defended = 0
            return 1
        else:
            return 0
    
class GameField:
    def __init__(self, deck: Deck, players: list):
        self.deck = deck
        self.players = players
        self.challenges = []
        self.open_attack = 0

    def set_defender(self, defender: Player):
        self.defender = defender

    def attack(self, card: Card, attacker: Player):
        if(card.value == "Joker"):
            return 0
        
        can_play = 0
        if(len(self.challenges) == 0):
            can_play = 1
        else:
            for n in self.challenges:
                if n.offense.value == card.value:
                    can_play = 1
                if n.defended == 1:
                    if n.defense.value == card.value:
                        can_play == 1
                    if n.defense.value == "Joker":
                        can_play == 0
                        break

        if(can_play == 1):
            challenge = Challenge(card, attacker)
            self.challenges.append(challenge)
            self.open_attack = 1
