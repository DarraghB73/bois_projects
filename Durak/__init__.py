from game_classes import Card, Deck

def main():

    card_list = []
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    #create 52 cards and adds them to the card_list
    for suit in suits:
        for value in values:
            card = Card(suit, value)
            card_list.append(card)

    #initialise deck with the 52 cards
    deck = Deck(card_list)

    #shuffle the deck
    deck.shuffle()

    #deal out a hand of 7 cards
    hand = deck.deal_hand(7)
    
    #print out the hand
    for card in hand:
        print(card)

main()