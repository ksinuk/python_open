import sys
sys.stdin = open("input.txt", "r")

N = int(input())
for index in range(1,N+1):
    num = int(input())
    list_in = list(map(int,input().split()))
    list_nasa = [[0,0] for i in range(num)]
    for i in range(num):
        list_nasa[i][0] = list_in[2*i]
        list_nasa[i][1] = list_in[2*i+1]

    list_out = [[0, 0] for i in range(num)]
    #입력 완료-------------------------------------

    list_front = [0]*num
    list_end = [0]*num
    for i in range(num):
        list_front[i] = list_nasa[i][0]
        list_end[i] = list_nasa[i][1]

    for i in range(num):
        if list_front[i] not in list_end:
            list_out[0] = list_nasa[i][:]

    end = list_out[0][1]
    for i in range(1,num):
        for j in range(num):
            if end == list_front[j]:
                list_out[i] = list_nasa[j][:]
                end = list_nasa[j][1]
                break

    #출력 완료------------------------------------
    print(f"#{index}",end='')
    for i in range(num):
        print(f" {list_out[i][0]}",end='')
        print(f" {list_out[i][1]}", end='')
    print()