import sys
sys.stdin = open("사냥꾼_input.txt","r")

for __ in range(1):
    size = int(input())
    maps = [[] for i in range(size)]
    for i in range(size):
        maps[i] = list(input())

    hunters = []
    for y in range(size):
        for x in range(size):
            if maps[y][x]=='1':
                hunters.append([y,x])
    arrows = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    rabbit = 0
    for hunter in hunters:
        for arrow in arrows:
            now = [hunter[0] , hunter[1]]

            while 1:
                now[0] , now[1] = now[0]+arrow[0] , now[1]+arrow[1]
                if now[0]<0 or now[1]<0 or now[0]>=size or now[1]>=size or maps[now[0]][now[1]]=='0':
                    break
                elif maps[now[0]][now[1]]=='2':
                    rabbit+=1
                    maps[now[0]][now[1]] = '9'
        
    print(rabbit)




    
    
      