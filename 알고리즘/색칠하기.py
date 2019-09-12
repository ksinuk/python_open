import sys
sys.stdin = open("색칠하기.txt","r")

ysize, xsize, num = map(int,input().split())
table = [[0 for x in range(xsize)] for y in range(ysize)]

max_color = 0
for i in range(num):
    fy , fx , ly , lx , color = map(int,input().split())
    if(max_color > color): continue
    max_color = color

    for y in range(fy,ly+1):
        for x in range(fx,lx+1):
            table[y][x] = color

out = 0
for y in range(ysize):
    for x in range(xsize):
        if max_color == table[y][x]: out+=1

print(out)





