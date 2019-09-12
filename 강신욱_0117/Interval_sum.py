import sys
sys.stdin = open("interval_sum_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    line_size , scale = map(int, input().split())
    list_in = list(map(int, input().split()))
    list_y = [0]*(line_size-scale+1)

    for i in range(line_size-scale+1):
        temp=0
        for x in range(scale):
            temp += list_in[i+x]
        list_y[i] = temp
    
    min=list_y[0]
    max=list_y[0]
    for i in range(line_size-scale+1):
        if max<list_y[i]:
            max = list_y[i]
        if min>list_y[i]:
            min = list_y[i]
    
    print(f"#{test_case} {max-min}")
