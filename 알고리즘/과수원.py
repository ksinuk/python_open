import sys
sys.stdin = open("과수원_input.txt","r")

for __ in range(1):
    size = int(input())
    maps = [[] for i in range(size)]
    for i in range(size):
        maps[i] = list(input())
        maps[i] = list(map(int,maps[i]))
    
    sum_y = [0 for i in range(size)]
    sum_x = [0 for i in range(size)]
    sum_max = 0

    for y in range(size):
        temp = 0
        for x in range(size):
            temp += maps[y][x]
        if y>0:
            sum_y[y] = temp + sum_y[y-1]
        else:
            sum_y[y] = temp
    sum_max = sum_y[size-1]
    if sum_max%2 or (sum_max//2) not in sum_y:
        print("-1")
        break
    for x in range(size):
        temp = 0
        for y in range(size):
            temp += maps[y][x]
        if x>0:
            sum_x[x] = temp + sum_x[x-1]
        else:
            sum_x[x] = temp     
    if (sum_max//2) not in sum_y:
        print("-1")
        break

    out_y = 0
    for i in range(size):
        if sum_y[i] == sum_max//2:
            out_y+=1
        elif sum_y[i] > sum_max//2:
            break
    out_x = 0
    for i in range(size):
        if sum_x[i] == sum_max//2:
            out_x+=1
        elif sum_x[i] > sum_max//2:
            break

    print(out_y*out_x)