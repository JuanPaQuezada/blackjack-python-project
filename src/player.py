#player class 
class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
    def add_card(self, card):
        self.hand.append(card)
    def calculate_score(self):
        score=0
        aces=0
        for card in self.hand:
            if card.rank in ["J","Q","K"]:
                score+=10
            elif card.rank=="A":
                score+=11
                aces+=1
            else:
                score+=int(card.rank)

        while score>21 and aces>0:
            score-=10
            aces-=1

        return score


