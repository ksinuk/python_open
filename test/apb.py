class p:
    num=0
    def __init__(self , name='temp'):
        self.name=name
        p.num+=1
    def print(self):
        print(self.name)

a=p()
a.add = 1
print(a.add)