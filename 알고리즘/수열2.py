import sys
sys.stdin = open("수열2.txt","r")

def cal_main(size):
    table = [[] for i in range(size)]
    for i in range(size):
        table[i] = list(map(int,input().split()))

    out = 0
    for y in range(size):
        step = 0
        lens = 0
        for x in range(1,size):
            if abs(table[y][x]-table[y][x-1])!=1:
                step = 0
                out = lens if lens>out else out
                lens = 0
            elif step==0:
                step = table[y][x]-table[y][x-1]
                lens = 2
            elif step == table[y][x]-table[y][x-1]:
                lens+=1
            else:
                step = 0
                out = lens if lens>out else out
                lens = 0
        out = lens if lens>out else out
    for x in range(size):
        step = 0
        lens = 0
        for y in range(1,size):
            if abs(table[y][x]-table[y-1][x])!=1:
                step = 0
                out = lens if lens>out else out
                lens = 0
            elif step==0:
                step = table[y][x]-table[y-1][x]
                lens = 2
            elif step == table[y][x]-table[y-1][x]:
                lens+=1
            else:
                step = 0
                out = lens if lens>out else out
                lens = 0
        out = lens if lens>out else out

    return out

#---------------------------------
N = int(input())
for i in range(N):
    size = int(input())
    print(cal_main(size))