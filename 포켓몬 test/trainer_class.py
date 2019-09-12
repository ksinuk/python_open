import random
from item_class import *
from pokemon_class import *

class Trainer:
    def __init__(self,name="트레이너",level=3):
        self.name =name
        self.pokermon_list = []
        self.pokermon_list.append(Pokemon("이상해씨","이상해씨",level,name))
        self.pokermon_list.append(Pokemon("파이리","파이리",level,name))
        self.pokermon_list.append(Pokemon("꼬부기","꼬부기",level,name))
        self.items = Item()
        self.level = level
        self.now_pokemon = self.pokermon_list[0]


    def return_pokemon(self,my):
        self.pokermon_list.pop(0)
        if len(self.pokermon_list):
            self.now_pokemon=self.pokermon_list[0]
            print(f"_{self.name}은 {self.now_pokemon.name}을 꺼냈다!")

            return 0
        else :
            return "win"

    def use_turn(self,my):
        temp=0
        for i in self.now_pokemon.skill_list:
            if i.pp>0:
                temp+=1

        num=random.randint(0,temp-1)
        while self.now_pokemon.skill_list[num].pp<=0:
            num=(num+1)%temp

        
        self.now_pokemon.skill_list[num].use(self.now_pokemon,my.now_pokemon)
        if self.now_pokemon.hp<=0:
            print(f"_{self.now_pokemon.name}이 쓰려 젔다.")
            print(f"{my.now_pokemon.name}은 경험치 {self.now_pokemon.level*50}을 획득했다.")
            my.now_pokemon.add_score(self.now_pokemon.level*50)
            if self.return_pokemon(my)=="win":
                return "win"
        if my.now_pokemon.hp<=0:
            print(f"{my.now_pokemon.name}이 쓰려 젔다.")
            if my.return_pokemon()=='lose':
                return "lose"

        my.print_pokemon(self.now_pokemon)

        return 0

class jiou:
    def __init__(self,name,starting):
        self.name =name
        self.pokermon_list = [starting]
        self.items = Item()
        self.level = 5
        self.now_pokemon = self.pokermon_list[0]
        self.money = 100000

    def store(self):
        print("0. 돌아가기")
        print("1. 20hp 포션 : 10원")
        print("2. 50hp 포션 : 50원")
        print("3. 몬스터볼(x1) : 10원")
        print("4. 몬스터볼(x2) : 40원")
        print("5. 몬스터볼(x3) : 90원")
        print("6. 마스터볼 : 1000원")
        print(f"보유한 금액 : {self.money}")
        num=0
        while 1:
            num = input("무엇을 선택하시겠습니까? : ")
            num = int(num)
            if not(0<=num and num<7):
                print("제대로 선택하세요")
            else :
                break

        if num==0:
            return 0
        elif num==1:
            if self.money>=10:
                self.money-=10
                self.items.portion.p20+=1
            else:
                print("돈이 부족합니다.")
        elif num==2:
            if self.money>=50:
                self.money-=50
                self.items.portion.p50+=1
            else:
                print("돈이 부족합니다.")
        elif num==6:
            if self.money>=1000:
                self.money-=1000
                self.items.monsterball.ball_list[3]+=1
            else:
                print("돈이 부족합니다.")
        else :
            num-=3
            if self.money>=num*num*100:
                self.money-=num*num*100
                self.items.monsterball.ball_list[num]+=1
            else:
                print("돈이 부족합니다.")
        
        return 0

    def clinic(self):
        for pet in self.pokermon_list:
            pet.hp = pet.hp_max
            pet.conditions = []
            for skill in pet.skill_list:
                skill.pp = skill.pp_max

        return 0
        

    def return_pokemon(self):
        temp=0
        for i in self.pokermon_list:
            if i.hp>0:
                temp+=1

        if temp:
            print(f"돌아와! {self.now_pokemon.name}!!")
            print(f'포켓몬을 선택하세요')
            print(f"0번 = 돌아가기")

            num = 0
            out=0
            for i in range(1,len(self.pokermon_list)+1):
                pokemon = self.pokermon_list[i-1]
                print(f"{i}번 = 이름: {pokemon.name} , 레벨: {pokemon.level} , hp: {pokemon.hp}")
                if pokemon.hp>0:
                    out+=1
            while 1:
                num = input("몇 번째 포켓몬을 선택하시겠습니까? : ")
                num = int(num)
                if not(0<= num and num<=i):
                    print("제대로 선택하세요")
                elif self.pokermon_list[num-1].hp<=0:
                    print("체력이 0인 포켓몬은 선택할 수 없습니다.")
                else :
                    break

            self.now_pokemon=self.pokermon_list[num-1]
            print(f"가라 {self.now_pokemon.name}! 너로 정했다!")

            print(f"return_pokemon out : {out}")
            return out
        else :
            print(f"{self.name}은 패배했다!")
            print(f"{self.name}은 눈 앞이 깜깜해 졌다!")

            return "lose"

    def select_item(self,cut,listx=[]):
        while 1:
            num = input("몇 번째 아이템을 선택하시겠습니까? : ")
            num = int(num)
            if not(0<=num and num<=cut):
                print("제대로 선택하세요")
            elif listx[num-1]==0:
                print("아이템의 갯수가 0개 입니다.")
            else :
                return num

    def use_item(self,other_pokemon):
        while 1:
            print("사용할 아이템을 선택하세요")
            print("0번 = 돌아가기")
            print(f"1번 = 포션")
            num = 0
            while 1:
                num = input("몇 번째 아이템을 선택하시겠습니까? : ")
                num = int(num)
                if not(0<=num and num<=1):
                    print("제대로 선택하세요")
                else:
                    break


            if num==1:
                print("0번 = 돌아가기")
                print(f"1번 = 20hp 치료제 : {self.items.portion.p20}")
                print(f"1번 = 50hp 치료제 : {self.items.portion.p50}")
                num_portion=self.select_item(2,[self.items.portion.p20,self.items.portion.p50])

                if num_portion==0:
                    continue
                elif num_portion==1:
                    print(f"20hp 치료제를 사용했습니다.")
                    self.items.portion.use(self.now_pokemon,20)
                elif num_portion==2:
                    print(f"50hp 치료제를 사용했습니다.")
                    self.items.portion.use(self.now_pokemon,50)
            else:
                break

        self.print_pokemon(other_pokemon)# 몬스터 상태창 출력

        return 0

    def print_pokemon(self,other_pokemon):
        print("나의 포켓몬")
        self.now_pokemon.print()
        print("\n상대하는 포켓몬")
        other_pokemon.print()
        print('\n')

    def hunt_pokemon(self,pokemon):
        if pokemon.trainer_name:
            print("도둑질은 안돼!")
            return 1
        if len(self.pokermon_list)>=6:
            print("더 이상 잡을 수 없다!")
            return 1

        my_ball = self.items.monsterball
        print(f"0번 = 돌아가기")
        print(f"1번 : ball_x1 = {my_ball.ball_list[0]}")
        print(f"2번 : ball_x2 = {my_ball.ball_list[1]}")
        print(f"3번 : ball_x4 = {my_ball.ball_list[2]}")
        print(f"4번 : master_ball = {my_ball.ball_list[3]}")
        num=0
        while 1:
            num = input("몇 번째 몬스터볼을 선택하시겠습니까? : ")
            num = int(num)
            if not(0<=num and num<5):
                print("제대로 선택하세요")
            elif num==0:
               return 0
            elif my_ball.ball_list[num-1]<=0:
                print("더이상 가지고 있지 않은 볼입니다.")
            else :
                break

        result = my_ball.make_result(num-1,pokemon)
        if result=='catch':
            print(f"{pokemon.name}을 포획했다!")
            self.pokermon_list.append(pokemon)

            return 'catch'
        else :
            print(f"포획 실패!!!")
            return 0

    def use_skill(self,other_pokemon,trainer=0):

        print(f"0번 = 돌아가기")
        for i in range(1,len(self.now_pokemon.skill_list)+1):
            print(f"{i}번 : {self.now_pokemon.skill_list[i-1].name} , pp = {self.now_pokemon.skill_list[i-1].pp}")
        num=0
        while 1:
            num = input("몇 번째 스킬을 선택하시겠습니까? : ")
            num = int(num)
            if not(0<=num and num<=len(self.now_pokemon.skill_list)+1):
                print("제대로 선택하세요")
            elif self.now_pokemon.skill_list[num-1].pp<=0:
                print("더 이상 사용 할 수 없는 스킬입니다.")
            else :
                break

        self.now_pokemon.skill_list[num-1].use(self.now_pokemon,other_pokemon)
        if self.now_pokemon.hp<=0:
            print(f"{self.now_pokemon.name}이 쓰려 젔다.")
            if self.return_pokemon()=="lose":
                return "lose"
        if other_pokemon.hp<=0:
            print(f"{other_pokemon.name}이 쓰려 젔다.")
            print(f"{self.now_pokemon.name}은 경험치 {other_pokemon.level*50}을 획득했다.")
            self.now_pokemon.add_score(other_pokemon.level*50)

            if trainer==0 or trainer.return_pokemon(self)=="win":
                lv = other_pokemon.level
                print(f"{self.name}은 승리했다!")
                if trainer!=0:
                    lv = trainer.level
                print(f"{self.name}은 돈 {lv*100}원을 획득했다.")
                self.money+=lv*100

                return "win"

        self.print_pokemon(other_pokemon)

        return 0


        

        

        
        


        
        
        