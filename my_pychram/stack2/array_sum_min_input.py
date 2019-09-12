import sys
sys.stdin = open("array_sum_min_input.txt", "r")

def cal(table,min,sum,p,size,arr):
    sum+=table[p][arr[p]]
    if sum>=min:return min

    if p!=size-1:
        for i in range(p+1,size):
            arr[p+1], arr[i] = arr[i], arr[p+1]
            min = cal(table, min, sum, p+1, size, arr)
            arr[p+1], arr[i] = arr[i], arr[p+1]
    else:
        min = sum if min>sum else min

    return min


T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    table = [[] for i in range(size)]

    for i in range(size):
        table[i] = list(map(int , input().split()))

    min = 0
    for i in range(size):
        min += table[i][i]

    arr = [i for i in range(size)]
    for i in range(size):
        arr[0] , arr[i] = arr[i] , arr[0]
        min = cal(table,min,0,0,size,arr)
        arr[0], arr[i] = arr[i], arr[0]

    print(f"#{test_case} {min}")