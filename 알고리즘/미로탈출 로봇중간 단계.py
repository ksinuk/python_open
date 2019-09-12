import sys
sys.stdin = open("미로탈출_로봇중간_단계_input.txt","r")


for __ in range(1):
    size = int(input())
    maps = [[] for i in range(size)]
    for i in range(size):
        maps[i] = list(input())
    arrow_in = list(map(int,input().split()))
    
    arrows = [[1,0],[0,1],[-1,0],[0,-1]]
    for i in range(4):
        if arrow_in[i]==1:
            arrows[i] = [1,0]
        elif arrow_in[i]==2:
            arrows[i] = [0,-1]
        elif arrow_in[i]==3:
            arrows[i] = [-1,0]
        elif arrow_in[i]==4:
            arrows[i] = [0,1]
    arrow = 0
    now = [0,0]
    out = 0

    while 1:
        dy , dx = arrows[arrow][0] , arrows[arrow][1]
        next_y , next_x = now[0]+dy ,  now[1]+dx
        if next_y <0 or next_y >=size or next_x <0 or next_x >=size or maps[next_y][next_x] == '1':
            arrow = (arrow+1)%4
        elif maps[next_y][next_x] == '2':
            break
        else:
            maps[now[0]][now[1]] = '2'
            now[0] , now[1] = next_y , next_x
            out+=1
    
    print(out)


