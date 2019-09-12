import sys
sys.stdin = open("도넛츠_합계.txt","r")


for __ in range(1):
    size, donut_size = map(int,input().split())
    maps = [[] for i in range(size)]
    for i in range(size):
        maps[i] = list(map(int , input().split()))

    max_out = 0
    for y in range(size-donut_size+1):
        for x in range(size-donut_size+1):
            out = sum(maps[y][x:x+donut_size]) + sum(maps[y+donut_size-1][x:x+donut_size])
            for yy in range(y+1,y+donut_size-1):
                out += maps[yy][x] + maps[yy][x+donut_size-1]
            if out > max_out:
                max_out = out
    
    print(max_out)


