import sys
sys.stdin = open("최소_비용_input.txt", "r")
#---------------------------------------------
dy = [0,-1,0,1]
dx = [1,0,-1,0]
#---------------------------------------------
#---------------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    table = [[] for i in range(size)]
    for i in range(size):
        table[i] = list(map(int,input().split()))
    maps = [[0 for j in range(size)] for i in range(size)]
    #----------------------------------------------
    start = [0,0]
    last = [size-1,size-1]

    qu = [0]*10000
    front , end = 0,1
    qu[0] = start
    maps[start[0]][start[1]] = 1

    while front<end:
        now = qu[front][:];front+=1
        if now==last:
            break
        
        for i in range(4):
            nexta = [now[0]+dy[i],now[1]+dx[i]]
            if nexta[0]<0 or nexta[1]<0 or nexta[0]>=size or nexta[1]>=size: continue

            temp = maps[now[0]][now[1]]+1
            if table[nexta[0]][nexta[1]] > table[now[0]][now[1]]:
                temp += table[nexta[0]][nexta[1]] - table[now[0]][now[1]]
                
            if maps[nexta[0]][nexta[1]]==0:
                maps[nexta[0]][nexta[1]] = temp
                qu[end] = nexta[:];end+=1
                for i in range(end-1,front,-1):
                    if maps[qu[i][0]][qu[i][1]] < maps[qu[i-1][0]][qu[i-1][1]]:
                        qu[i] , qu[i-1] = qu[i-1] , qu[i]
                    else:
                        break
            elif maps[nexta[0]][nexta[1]]>temp:
                maps[nexta[0]][nexta[1]] = temp
                for k in range(front,end):
                    if qu[k] == nexta:
                        for i in range(k,front,-1):
                            if maps[qu[i][0]][qu[i][1]] < maps[qu[i-1][0]][qu[i-1][1]]:
                                qu[i] , qu[i-1] = qu[i-1] , qu[i]
                            else:
                                break

    print("#{} {}".format(test_case,maps[last[0]][last[1]]-1))