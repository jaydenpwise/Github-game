import random
from deck import Deck
from player import Player

'''Two-Deck War
cards.py  - Card class (suit, rank, value)
deck.py   - Deck class (builds 52 Card objects, shuffles them)
player.py - Player class (draw card, collect cards, check if player has cards)
main.py   - runs the game
'''


#Plays one round, including any wars. Returns the winning player.
def play_round(player1, player2):
    card1 = player1.draw_card()
    card2 = player2.draw_card()

    print(f"{player1.name} drew the {card1}.")
    print(f"{player2.name} drew the {card2}.")

    #Every card played this round goes into this list so the winner gets all of them
    cards_played = [card1, card2]
    was_war = False

    #Keep going to war as long as the cards tie
    while card1.value == card2.value:
        print("War!")
        was_war = True

        #If a player runs out of cards during a war, they lose the war
        if not player1.has_cards():
            print(f"{player1.name} has no cards left to play.")
            return finish_round(player2, cards_played, was_war)
        if not player2.has_cards():
            print(f"{player2.name} has no cards left to play.")
            return finish_round(player1, cards_played, was_war)

        card1 = player1.draw_card()
        card2 = player2.draw_card()

        print(f"{player1.name} drew the {card1}.")
        print(f"{player2.name} drew the {card2}.")

        cards_played.append(card1)
        cards_played.append(card2)

    #The higher card value wins (2 is lowest, Ace is highest)
    if card1.value > card2.value:
        return finish_round(player1, cards_played, was_war)
    else:
        return finish_round(player2, cards_played, was_war)


#Gives the winner the cards and prints who won
def finish_round(winner, cards_played, was_war):
    if was_war:
        print(f"{winner.name} wins the war!")
    else:
        print(f"{winner.name} wins the round!")

    #Shuffle the won cards so the game can't get stuck repeating the same pattern forever
    random.shuffle(cards_played)
    winner.collect_cards(cards_played)
    return winner


#Main
def main():
    print("Welcome to Two-Deck War!")

    #Each player gets their own full deck
    deck1 = Deck()
    deck2 = Deck()

    #Shuffle the decks to randomize the order of the cards
    deck1.shuffle()
    deck2.shuffle()

    player1 = Player("Player 1", deck1.cards)
    player2 = Player("Player 2", deck2.cards)

    #Battle of the decks - keep playing rounds until someone is out of cards
    while player1.has_cards() and player2.has_cards():
        print()
        play_round(player1, player2)

        print(f"{player1.name} has {player1.card_count()} cards.")
        print(f"{player2.name} has {player2.card_count()} cards.")

        if player1.has_cards() and player2.has_cards():
            input("Press Enter to play the next round.")

    #Whoever still has cards has collected all of them
    if player1.has_cards():
        winner = player1
    else:
        winner = player2

    print()
    print(f"{winner.name} has collected all of the cards.")
    print(f"{winner.name} wins the game!")


if __name__ == "__main__":
    main()
