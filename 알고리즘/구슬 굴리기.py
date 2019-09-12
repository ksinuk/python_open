import sys
sys.stdin = open("구슬_굴리기_input.txt","r")

def cal_turn(turn):
    if turn==1: return [-1,0]
    elif turn==2: return [1,0]
    elif turn==3: return [0,-1]
    else: return [0,1]

for __ in range(2):
    size_x , size_y = map(int,input().split())
    table = [[] for i in range(size_y)]
    for y in range(size_y):
        table[y] = list(map(int,list(input())))
    turn_size = int(input())
    turns = list(map(int,input().split()))
    out = 1

    now = [0,0]
    for x in range(size_x):
        ok=1
        for y in range(size_y):
            if table[y][x]==2:
                now[0] , now[1] = y,x
                table[y][x] = 8
                ok=0
                break
        if ok==0:
            break

    for turn in turns:
        dyx = cal_turn(turn)

        while 1:
            next_yx = [ now[0]+dyx[0] , now[1]+dyx[1] ]
            if next_yx[0]<0 or next_yx[1]<0 or next_yx[0]>=size_y or next_yx[1]>=size_x:
                break
            elif table[next_yx[0]][next_yx[1]]==1:
                break
            else:
                if table[next_yx[0]][next_yx[1]]==0:
                    table[next_yx[0]][next_yx[1]] = 8
                    out +=1
                now[0] , now[1] = next_yx[0] , next_yx[1]
    
    print(out)



        

                