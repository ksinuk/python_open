import sys
sys.stdin = open("chairman_input.txt","r")

N = int(input())
for __ in range(N):
    table = [[0,0,0] , [0,0,0] , [0,0,0]]
    size = int(input())
    for i in range(size):
        a,b,c = map(int, input().split())
        table[0][a-1] += 1
        table[1][b-1] += 1
        table[2][c-1] += 1

    sum1 = table[0][0] + 2*table[0][1] + 3*table[0][2]
    sum2 = table[1][0] + 2*table[1][1] + 3*table[1][2]
    sum3 = table[2][0] + 2*table[2][1] + 3*table[2][2]

    if sum1>sum2 and sum1>sum3: print(f"1 {sum1}")
    elif sum2>sum1 and sum2>sum3: print(f"2 {sum2}")
    elif sum3>sum1 and sum3>sum2: print(f"3 {sum3}")
    elif sum1==sum2 and sum1>sum3:
        if table[0][2]>table[1][2] or table[0][2]==table[1][2] and  table[0][1]>table[1][1]: print(f"1 {sum1}")
        elif table[0][2]<table[1][2] or table[0][2]==table[1][2] and  table[0][1]<table[1][1]: print(f"2 {sum2}")
        else: print(f"0 {sum1}")
    elif sum1==sum3 and sum1>sum2:
        if table[0][2]>table[2][2] or table[0][2]==table[2][2] and  table[0][1]>table[2][1]: print(f"1 {sum1}")
        elif table[0][2]<table[2][2] or table[0][2]==table[2][2] and  table[0][1]<table[2][1]: print(f"3 {sum3}")
        else: print(f"0 {sum1}")
    elif sum2==sum3 and sum2>sum1:
        if table[1][2]>table[2][2] or table[1][2]==table[2][2] and  table[1][1]>table[2][1]: print(f"2 {sum2}")
        elif table[1][2]<table[2][2] or table[1][2]==table[2][2] and  table[1][1]<table[2][1]: print(f"3 {sum3}")
        else: print(f"0 {sum2}")
    else:# sum1==sum2==sum3
        if table[2][2] > table[0][2] and table[2][2] > table[1][2]: print(f"3 {sum3}")
        elif table[1][2] > table[0][2] and table[1][2] > table[2][2]: print(f"2 {sum2}")
        elif table[0][2] > table[1][2] and table[0][2] > table[2][2]: print(f"1 {sum1}")

        elif table[2][2] == table[0][2] and table[2][2] > table[1][2]:
            if table[2][1]>table[0][1]: print(f"3 {sum3}")
            elif table[2][1]<table[0][1]: print(f"1 {sum1}")
            else: print(f"0 {sum1}")
        elif table[1][2] == table[2][2] and table[1][2] > table[0][2]:
            if table[2][1]>table[1][1]: print(f"3 {sum3}")
            elif table[2][1]<table[1][1]: print(f"2 {sum2}")
            else: print(f"0 {sum1}")
        elif table[0][2] == table[1][2] and table[0][2] > table[2][2]:
            if table[1][1]>table[0][1]: print(f"2 {sum2}")
            elif table[1][1]<table[0][1]: print(f"1 {sum1}")
            else: print(f"0 {sum1}")
        else: #table[0][2] == table[1][2] and table[0][2] == table[2][2]:
            if table[0][1] == table[1][1] and table[0][1] < table[2][1]: print(f"3 {sum3}")
            elif table[0][1] == table[2][1] and table[0][1] < table[1][1]: print(f"2 {sum2}")
            elif table[1][1] == table[2][1] and table[1][1] < table[0][1]: print(f"1 {sum1}")
            else: print(f"0 {sum1}")
    





