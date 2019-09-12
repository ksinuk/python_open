from skill_class import *

class Pokemon_kind:
    kind_high = ['이상해꽃','리자몽','거북왕','피죤투','라이츄']
    kind_mid = ['이상해풀','리자드','어니부기','피죤','피카츄']
    kind_low = ['이상해씨','파이리','꼬부기','구구']

    kind_leaf = ['이상해씨','이상해풀','이상해꽃']
    kind_water = ['꼬부기','어니부기','거북왕']
    kind_fire = ['리자몽','리자드','파이리']
    kind_air = ['구구','피죤','피죤투']
    kind_elec = ['라이츄','피카츄']

    def __init__(self,name):
        self.name = name

    def skill(self,skill_list,name,level):
        listx = []
        for i in skill_list:
            listx.append(i.name) 

        list_out = []
        if self.name in Pokemon_kind.kind_leaf:
            list_out = ["몸통박치기","덩쿨채찍"]
            if level>=10:
                list_out.append("잎날가르기")
            if level>=15:
                list_out.append("솔라빔")
        if self.name in Pokemon_kind.kind_water:
            list_out = ["몸통박치기","물대포"]
            if level>=10:
                list_out.append("파도타기")
            if level>=15:
                list_out.append("하이드로펌프")
        if self.name in Pokemon_kind.kind_fire:
            list_out = ["몸통박치기","불꽃세례"]
            if level>=10:
                list_out.append("화염방사")
            if level>=15:
                list_out.append("플레어드라이브")  
        if self.name in Pokemon_kind.kind_air:
            list_out = ["몸통박치기","날개치기"]
            if level>=10:
                list_out.append("공중날기")
            if level>=15:
                list_out.append("불새")
        if self.name in Pokemon_kind.kind_elec:
            list_out = ["몸통박치기","전기쇼크"]
            if level>=10:
                list_out.append("10만볼트")
            if level>=15:
                list_out.append("번개")

        for y in list_out:
            if y not in listx:
                if name:
                    print(f"{name}은 스킬 {y}를 익혔다.")
                skill_list.append(Skill(y))
                
        return  skill_list


    def types(self):
        if self.name in Pokemon_kind.kind_leaf:
            return 'leaf'
        if self.name in Pokemon_kind.kind_water:
            return 'water'
        if self.name in Pokemon_kind.kind_fire:
            return 'fire'
        if self.name in Pokemon_kind.kind_air:
            return 'air'
        if self.name in Pokemon_kind.kind_elec:
            return 'elec'

        return 0

    def hp(self,level):
        if self.name in Pokemon_kind.kind_high:
            return 120+level
        elif self.name in Pokemon_kind.kind_mid:
            return 70+level
        else:
            return 50+level

    def hit_rate(self,level): #float
        return 0.9+level/100.0
    
    def avoid_rate(self,level): #float
        return level/100.0

    def hunt_rate(self,level):
        return level/100.0

    def next_level(self):
        if self.name in Pokemon_kind.kind_high:
            return 1200
        elif self.name in Pokemon_kind.kind_mid:
            return 15
        else:
            return 10


    def next_pokemon(self):
        if self.name in Pokemon_kind.kind_high:
            return 'end'
        elif self.name in Pokemon_kind.kind_mid:
            if self.name=='피카츄':
                return '라이츄'
            if self.name=='피죤':
                return '피죤투'
            if self.name=='이상해풀':
                return '이상해꽃'
            if self.name=='리자드':
                return '리자몽'
            if self.name=='어니부기':
                return '거북왕'
        else:
            if self.name=='구구':
                return '피죤'
            if self.name=='이상해씨':
                return '이상해풀'
            if self.name=='파이리':
                return '리자드'
            if self.name=='꼬부기':
                return '어니부기'


        return 10