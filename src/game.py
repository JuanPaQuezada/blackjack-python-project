
from src.player import Player
from src.cards import Deck
from src.utils import *
from InquirerPy import inquirer


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player=Player("Jugador_1")
        self.dealer=Player("Dealer")
    def setup_round(self):
        self.deck.shuffle()
        for _ in range(2):
            new_card_player=self.deck.deal()
            self.player.add_card(new_card_player)
            new_card_bot=self.deck.deal()
            self.dealer.add_card(new_card_bot)
    def player_turn(self):
        while True:
            print(f"Score: {self.player.calculate_score()}")
            chosen_option=inquirer.select(
                    message="It's your turn. What would you like to do?",
                    choices=[
                        "Hit",
                        "Stand"
                    ],
                    pointer=">"
            ).execute()
            if chosen_option=="Hit":
                self.player.add_card(self.deck.deal())
                if self.player.calculate_score()>21:
                    print("You went over 21")
                    return False

            elif chosen_option=="Stand":
                return True

    def dealer_turn(self):
        while self.dealer.calculate_score()<17:
            self.dealer.add_card(self.deck.deal())
            print("The dealer hits...")

    def determine_winner(self):
        player_score=self.player.calculate_score()
        dealer_score=self.dealer.calculate_score()
        if dealer_score>21:
            print("Player wins")
        elif player_score > dealer_score:
            print("Player wins")
        elif player_score==dealer_score:
            print("draw")
        else:
            print("Dealer wins")

    def play(self):
        self.setup_round()
        player_is_alive=self.player_turn()
        if player_is_alive:
            self.dealer_turn()
            self.determine_winner()



