import sys
sys.stdin = open("보급로_input.txt", "r")

dy = [0,-1,0,1]
dx = [1,0,-1,0]
#-----------------------------------------



#-----------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    table = [[] for i in range(size)]
    for i in range(size):
        table[i] = list(map(int,list( input() ) ) )
    #-----------------------------------------------
    maps = [[-1 for j in range(size)] for i in range(size)]

    start = [0,0]
    last = [size-1,size-1]

    qu = [0]*10000
    front , end = 0,1
    qu[0] = start
    maps[start[0]][start[1]] = 0

    while front<end:
        now = qu[front];front+=1
        if now==last:
            break
        dist = maps[now[0]][now[1]]
        
        for i in range(4):
            nexta = [now[0]+dy[i],now[1]+dx[i]]
            if nexta[0]<0 or nexta[1]<0 or nexta[0]>=size or nexta[1]>=size: continue

            temp = dist + table[nexta[0]][nexta[1]]

            if maps[nexta[0]][nexta[1]]==-1:
                maps[nexta[0]][nexta[1]] = temp
                qu[end] = nexta;end+=1
                for i in range(end-1,front,-1):
                    if maps[qu[i][0]][qu[i][1]] < maps[qu[i-1][0]][qu[i-1][1]]:
                        qu[i] , qu[i-1] = qu[i-1] , qu[i]
                    else:
                        break

    print("#{} {}".format(test_case,maps[last[0]][last[1]]))