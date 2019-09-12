import sys
sys.stdin = open("연산_input.txt", "r")
#-----------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    x,y = map(int,input().split())

    qu = [0]*1000001
    visit = [0]*1000001
    front , end = 0,1
    qu[0] = x
    visit[x] = 1

    while front<end:
        now = qu[front];front+=1
        dist = visit[now]
        if now==y:
            break
        if now*2<=1000000 and visit[now*2]==0:
            visit[now*2] = dist+1
            qu[end] = now*2;end+=1
        if now+1<=1000000 and visit[now+1]==0:
            visit[now+1] = dist+1
            qu[end] = now+1;end+=1
        if now-1>0 and visit[now-1]==0:
            visit[now-1] = dist+1
            qu[end] = now-1;end+=1
        if now-10>0 and visit[now-10]==0:
            visit[now-10] = dist+1
            qu[end] = now-10;end+=1

    print("#{} {}".format(test_case,visit[y]-1))