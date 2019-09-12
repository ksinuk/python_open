import sys
sys.stdin = open("호수의_깊이.txt","r")

for __ in range(1):
    size = int(input())
    maps = [[] for i in range(size)]
    hosu = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        maps[i] = list(input().split())

    out = 0
    for y in range(size):
        in_hosu = 1
        for x in range(size):
            if maps[y][x] == '0': 
                in_hosu = 1
            else:
                hosu[y][x] = in_hosu
                in_hosu += 1
    for y in range(size):
        in_hosu = 1
        for x in range(size-1,-1,-1):
            if maps[y][x] == '0': 
                in_hosu = 1
            else:
                hosu[y][x] = in_hosu if in_hosu<hosu[y][x] else hosu[y][x]
                in_hosu += 1
    for x in range(size):
        in_hosu = 1
        for y in range(size):
            if maps[y][x] == '0': 
                in_hosu = 1
            else:
                hosu[y][x] = in_hosu if in_hosu<hosu[y][x] else hosu[y][x]
                in_hosu += 1
    for x in range(size):
        in_hosu = 1
        for y in range(size-1,-1,-1):
            if maps[y][x] == '0': 
                in_hosu = 1
            else:
                hosu[y][x] = in_hosu if in_hosu<hosu[y][x] else hosu[y][x]
                in_hosu += 1

    for y in range(size):
        for x in range(size):
            out += hosu[y][x]
    print(out)

