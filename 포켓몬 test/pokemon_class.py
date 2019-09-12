import random
from pokemon_list import *

class Pokemon:
    
    def __init__(self,name,kind_name,level,trainer_name=''):
        self.name = name #str
        kind=Pokemon_kind(kind_name)
        self.kind = kind #class pokemon_kind
        self.type1 = kind.types() # str
        self.level = level #int
        self.next_level = kind.next_level()
        self.hp_max = kind.hp(level) #int
        self.hp = self.hp_max #int
        self.hit_rate = kind.hit_rate(level) #float
        self.avoid_rate = kind.avoid_rate(level) #float
        self.hunt_rate = kind.hunt_rate(level) #int 1~100
        self.skill_list = []
        kind.skill(self.skill_list,'',level) #list class skill
        self.trainer_name = trainer_name
        self.score = 0

    def print(self):
        print(f"이름 : {self.name}")
        print(f"종류 : {self.kind.name}")
        print(f"타입 : {self.type1}")
        print(f"레벨 : {self.level}")
        print(f"경험치 : {self.score}")
        print(f"hp : {self.hp}")
        print(f"명중률 : {self.hit_rate}")
        print(f"회피률 : {self.avoid_rate}")

    
    def add_score(self,inx):
        if self.level<100:
            self.score+=inx

            while self.score >self.level*100 and self.level<100: 
                self.score-=self.level*100
                self.level+=1
                print(f"{self.name}의 레벨이 {self.level}이 됐다!")

            self.hp_max = self.kind.hp(self.level) #int
            self.hit_rate = self.kind.hit_rate(self.level) #float
            self.avoid_rate = self.kind.avoid_rate(self.level) #float
            self.hunt_rate = self.kind.hunt_rate(self.level) #int 1~100

        self.kind.skill(self.skill_list,self.name,self.level)
        if self.next_level<self.level:
            print(f"오잉?...{self.name}의 상태가?\n.\n.\n.")

            kind=Pokemon_kind(self.kind.next_pokemon())
            self.kind = kind #class pokemon_kind
            self.type1 = kind.types() # str
            self.next_level = kind.next_level()
            self.hp_max = kind.hp(self.level) #int
            self.hp = self.hp_max #int
            self.hit_rate = kind.hit_rate(self.level) #float
            self.avoid_rate = kind.avoid_rate(self.level) #float
            self.hunt_rate = kind.hunt_rate(self.level) #int 1~100
            print(f'{self.name}은 {self.kind.name}이 되었다!')

        

        return 0

    def wild_turn(self,my):
        temp=0
        for i in self.skill_list:
            if i.pp>0:
                temp+=1

        num=random.randint(0,temp-1)
        while self.skill_list[num].pp<=0:
            num=(num+1)%temp

        self.skill_list[num].use(self,my.now_pokemon)
        if self.hp<=0:
            print(f"_{self.name}이 쓰려 젔다.")
            print(f"{my.now_pokemon.name}은 경험치 {self.level*50}을 획득했다.")
            my.now_pokemon.add_score(self.level*50)
            return "win"
        if my.now_pokemon.hp<=0:
            print(f"{my.now_pokemon.name}이 쓰려 젔다.")
            if my.return_pokemon()=='lose':
                return "lose"

        my.print_pokemon(self)

        return 0

    