
# In this version of Blackjack I assume only player either makes/lose the money, 
# if he wins he wins twice his bet or else losses his bet.
#Also the deck is not as per the standard game, this is a assumed deck for LLD practice purpose.
import random 
class Deck:
    def __init__(self) -> None:
        self.cards = []
    def create_deck(self):
        self.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4,4, 4 ,4, 5 ,5 ,5 ,5 ,6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
         10, 10, 10, 10, 11, 11, 11,11]
        return 
    def shuffle_deck(self):
        random.shuffle(self.cards)
        return 
    def deal_cards(self):
        return random.choice(self.cards)

class Player:
    def __init__(self, amount) -> None:
        self.amount = amount
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
        return 
    def get_cards(self):
        return self.cards
    def place_bet(self, value):
        self.amount -= value
        return value
    def update_amount(self, value):
        self.amount += value

class Dealer:
    def __init__(self) -> None:
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
        return 
    def get_cards(self):
        return self.cards

class Blackjack:
    def __init__(self) -> None:
        pass 
    
    def checkresult(self, player, dealer, player_bet):
        if sum(player.get_cards()) > 17 or sum(dealer.get_cards()) == 17:
            print("Dealer won")
            return True
        elif sum(dealer.get_cards()) > 17 or sum(player.get_cards()) == 17:
            print("Player won")
            player.update_amount(2 * player_bet)
            return True 
        return False 

    def play(self):
        player = Player(1000)
        dealer = Dealer()
        deck = Deck()

        deck.create_deck()
        deck.shuffle_deck()
        while True:
            player_bet = player.place_bet(10)
            player_card = deck.deal_cards()
            player.add_card(player_card)

            dealer_card = deck.deal_cards()
            dealer.add_card(dealer_card) 

            if self.checkresult(player, dealer, player_bet):
                print("Game over!")
                return 

blackjack = Blackjack()
blackjack.play()