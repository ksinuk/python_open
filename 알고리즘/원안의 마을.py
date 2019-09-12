import sys
sys.stdin = open("원안의_마을.txt","r")

def search_center(maps,size):
    for y in range(size):
        for x in range(size):
            if maps[y][x] == '2':
                return [y,x]

def cal_range(center,house):
    dx , dy = center[0]-house[0] , center[1]-house[1]
    d2 = dx*dx+dy*dy
    d = d2**0.5
    d_int = int(d)
    if d2 != d_int**2:
        return d_int+1
    else:
        return d_int

#---------------------------------------------
for __ in range(1):
    size = int(input())
    maps = [[] for i in range(size)]
    for i in range(size):
        maps[i] = list(input())

    center=search_center(maps,size)

    out = 0
    for y in range(size):
        for x in range(size):
            if maps[y][x] == '1':
                temp = cal_range(center,[y,x])
                out = temp if temp > out else out
    
    print(out)

