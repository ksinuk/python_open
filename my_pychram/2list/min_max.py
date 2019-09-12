import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    listx = list(map(int, input().split()))
    min = listx[0]
    max = listx[0]
    for i in range(n):
        if min>listx[i]:min = listx[i]
        if max<listx[i]:max = listx[i]
    print(f"#{test_case} {max-min}")


