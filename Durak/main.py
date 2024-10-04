import random
from game_classes import Deck, GameField, Player

def main():
    
    #initialise deck with the 52 cards optionally add any number of jokers
    deck = Deck(jokers=2)
    # print(deck)

    #shuffle the deck
    deck.shuffle()

    #deal out a hand of 7 cards
    hand = deck.deal_hand(6)
    
    #print out the hand
    for card in hand:
        print(card)

    #initialise player list
    string_list = ["Conor", "Darragh", "Prof. Colm Ó Dúnlaing", "Johnny Clyde Vance III"]
    player_list = []
    for n in range(len(string_list)):
        player = Player(string_list[n])
        player.deal_hand(deck.deal_hand(6))
        player_list.append(player)
    random.shuffle(player_list)

    #initialise GameField
    gamefield = GameField(deck, player_list)
    gamefield.set_defender(gamefield.players[0])
    print(gamefield.defender)
    print(str(gamefield.players[1].hand[0]))
    print(gamefield.attack(gamefield.players[1].hand[0], gamefield.players[1]))

main()