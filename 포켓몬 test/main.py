import random

from trainer_class import *
from item_class import *
from skill_class import *
from pokemon_class import *
from pokemon_list import *

print("포켓몬스터 텍스트를 시작합니다.")
print("1. 처음부터")
print("2. 로드하기")
print("3. 종료하기")
num=0
while 1:
    num = input("무얷을 선택하시겠습니까? : ")
    num=int(num)
    if not(0<num and num<4):
        print("제대로 선택하세요")
    else :
        break


if num==3:
    exit()

me=0


if num==2:
    print("그런거 없다.")
    exit()
elif num==1:
    while 1:
        print("스타팅 포켓몬을 선택하세요")
        print("1. 파이리")
        print("2. 이상해씨")
        print("3. 꼬북이")
        num=0
        while 1:
            num = input("무얷을 선택하시겠습니까? : ")
            num = int(num)
            if not(0<num and num<4):
                print("제대로 선택하세요")
            else :
                break

        starting_name=0
        if num==1:
            starting_name='파이리'
        elif num==2:
            starting_name='이상해씨'
        elif num==3:
            starting_name='꼬부기'

        name = input("이름을 입력하세요 : ")
        print(f"이름 : {name} , 스타팅 포켓몬 : {num}")
        num = input("맞습니까?(y/n)")
        if num=='y' or num=='Y':
            me = jiou(name,Pokemon(starting_name,starting_name,5,name))
            break
    
    while 1:
        print("0. 종료하기")
        print("1. 사냥")
        print("2. 배틀")
        print("3. 치료")
        print("4. 상점")
        num=0
        while 1:
            num = input("무얷을 선택하시겠습니까? : ")
            num = int(num)
            if not(0<=num and num<6):
                print("제대로 선택하세요")
            else :
                break

        if num==0:
            exit()
        if num==4:
            me.store()
        elif num==3:
            me.clinic()
        elif num==1:
            lv=0
            while 1:
                lv = input("원하는 레벨을 입력하세요 : ")
                lv = int(lv)
                if not(0<=lv and lv<100):
                    print("제대로 선택하세요")
                else :
                    break

            kind_set = ['이상해씨','파이리','꼬부기','구구','피카츄']
            temp = random.randint(0,4)
            pokemon = Pokemon(kind_set[temp],kind_set[temp],lv)

            while 1:
                print("1. 스킬")
                print("2. 아이템")
                print("3. 포획")
                print("4. 몬스터 교환")
                print("5. 포켓몬 상태")
                lv=0
                while 1:
                    lv = input("무얷을 선택하시겠습니까? : ")
                    lv = int(lv)
                    if not(0<lv and lv<6):
                        print("제대로 선택하세요")
                    else :
                        break

                out=0
                if lv==5:
                    me.print_pokemon(pokemon)
                elif lv==4:
                    out = me.return_pokemon()
                elif lv==3:
                    out = me.hunt_pokemon(pokemon)
                elif lv==2:
                    out = me.use_item(pokemon)
                elif lv==1:
                    out = me.use_skill(pokemon)
                
                print('==============================')

                if out =='win' or out =='lose' or out =='catch':
                    break

                if lv!=5:
                    out = pokemon.wild_turn(me)
                    print('==============================')
                if out =='win' or out =='lose':
                    break
        elif num==2:
            lv=0
            while 1:
                lv = input("원하는 레벨을 입력하세요 : ")
                lv = int(lv)
                if not(0<=lv and lv<100):
                    print("제대로 선택하세요")
                else :
                    break

            trainer = Trainer("트레이너",lv)

            while 1:
                print("1. 스킬")
                print("2. 아이템")
                print("3. 포획")
                print("4. 몬스터 교환")
                print("5. 포켓몬 상태")
                lv=0
                while 1:
                    lv = input("무얷을 선택하시겠습니까? : ")
                    lv = int(lv)
                    if not(0<lv and lv<6):
                        print("제대로 선택하세요")
                    else :
                        break

                out=0
                if lv==5:
                    me.print_pokemon(pokemon)
                elif lv==4:
                    out = me.return_pokemon()
                elif lv==3:
                    out = me.hunt_pokemon(trainer.now_pokemon)
                elif lv==2:
                    out = me.use_item(trainer.now_pokemon)
                elif lv==1:
                    out = me.use_skill(trainer.now_pokemon,trainer)
                print('==============================')
                if out =='win' or out =='lose':
                    break

                if lv!=5:
                    out = trainer.use_turn(me)
                    print('==============================')
                if out =='win' or out =='lose':
                    break
                
            
        
        
        




