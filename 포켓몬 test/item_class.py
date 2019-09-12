import random

class Item:
    name = 'item'
    amount = 0

    def __init__(self):
        self.portion = Portion()
        self.monsterball = Monsterball()

class Portion:
    def __init__(self):
        self.p20 = 0
        self.p50 = 0

    def use(self,pokemon,px):
        pokemon.hp+=px
        if pokemon.hp>pokemon.hp_max:
            pokemon.hp=pokemon.hp_max

        if px==20:
            self.p20-=1
        if px==50:
            self.p50-=1

        return 0

class Monsterball:
    
    def __init__(self):
        self.ball_list = [0,0,0,0] #x1, x2, x3, masterball

    def make_result(self,ball,pokemon):
        self.ball_list[ball]-=1
        if ball==3:
            return 'catch'
        ball+=1

        a=random.random()*ball
        b=pokemon.hunt_rate
        if a>b:
            return 'catch'
        else:
            return 'no'



        return 0
