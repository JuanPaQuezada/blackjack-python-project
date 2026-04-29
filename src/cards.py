import random
#cartas
SUITS=["Corazones","Diamantes","Treboles","Picas"]
RANKS=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} de {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                new_card=Card(suit,rank)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        selection_card=self.cards.pop()
        return selection_card



#menu

#pantalla de ganador 

#pantalla de perder
