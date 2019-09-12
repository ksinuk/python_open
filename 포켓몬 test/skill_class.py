import random

class Skill:

    def __init__(self,name):
        self.name = name
        self.pp = Skill_list.pp_max(name)
        self.pp_max = self.pp
        self.type1 = Skill_list.make_type(name)


    def use(self,attaker,defender):
        self.pp-=1
        print(f"{attaker.name}은 {self.name}을 사용했다!")

        rate = attaker.hit_rate-defender.avoid_rate
        temp = random.random()*2-1
        if temp>rate:
            print("그러나 공격이 빗나갔다!")
            return 0
        
        if self.name=="마비" and "마비" not in defender.conditions:
            defender.conditions.append("마비")
            return 0
        elif self.name=="맹독" and "맹독" not in defender.conditions:
            defender.conditions.append("맹독")
            return 0
        elif self.name=="몸통박치기":
            defender.hp-=10
            return 0
        
        x = 1.0
        demege= 0
        if self.type1=='air':
            if defender.type1 =='leaf':
                x*=2
            if  defender.type1 =='elec':
                x*=0.5
        elif self.type1=='elec':
            if defender.type1 =='air' or defender.type1 =='water':
                x*=2
            if  defender.type1 =='leaf' or defender.type1 =='elec':
                x*=0.5
        elif self.type1=='leaf':
            if defender.type1 =='water':
                x*=2
            if  defender.type1 =='leaf' or defender.type1 =='fire' or defender.type1 =='air':
                x*=0.5
        elif self.type1=='fire':
            if defender.type1 =='leaf':
                x*=2
            if  defender.type1 =='fire' or defender.type1 =='water':
                x*=0.5
        elif self.type1=='water':
            if defender.type1 =='fire':
                x*=2
            if  defender.type1 =='leaf' or defender.type1 =='water':
                x*=0.5
        
        if self.name in Skill_list.skill_list_high:
            demege = 55*x
        elif self.name in Skill_list.skill_list_mid:
            demege = 35*x
        elif self.name in Skill_list.skill_list_low:
            demege = 15*x

        if x>1:
            print("효과는 굉장했다!")
        elif x<1:
            print("영 좋지 않은 공격이다.")

        defender.hp-=demege

        return 0


class Skill_list:
    skill_list_nomal = ["몸통박치기"] #pp : 100
    skill_list_leaf = ["덩쿨채찍","잎날가르기","솔라빔"] #pp : 50 20 10 , damege :15 35 55
    skill_list_fire = ["불꽃세례","화염방사","플레어드라이브"]
    skill_list_water = ["물대포","파도타기","하이드로펌프"]
    skill_list_air = ["날개치기","공중날기","불새"]
    skill_list_elec = ["전기쇼크","10만볼트","번개"]

    skill_list_high= ["솔라빔","플레어드라이브","하이드로펌프","불새","번개"]
    skill_list_mid= ["잎날가르기","화염방사","파도타기","공중날기","10만볼트"]
    skill_list_low= ["덩쿨채찍","불꽃세례","물대포","날개치기","전기쇼크"]

    @classmethod
    def pp_max(cls,name):
        if name in cls.skill_list_high:
            return 10
        if name in cls.skill_list_mid:
            return 20
        if name in cls.skill_list_low:
            return 50
        if name == "몸통박치기":
            return 100

        return -1

    @classmethod
    def make_type(cls,name):
        if name in cls.skill_list_leaf:
            return 'leaf'
        if name in cls.skill_list_fire:
            return 'fire'
        if name in cls.skill_list_water:
            return 'water'
        if name in cls.skill_list_air:
            return 'air'
        if name in cls.skill_list_elec:
            return 'elec'
        if name in cls.skill_list_nomal:
            return 'nomal'

        return -1
