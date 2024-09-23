from game_classes import Deck

def main():
    
    #initialise deck with the 52 cards optionally add any number of jokers
    deck = Deck(jokers=2)
    print(deck)

    #shuffle the deck
    deck.shuffle()

    #deal out a hand of 7 cards
    hand = deck.deal_hand(7)
    
    #print out the hand
    for card in hand:
        print(card)

main()
