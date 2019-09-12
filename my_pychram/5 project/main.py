import sys
sys.stdin = open("GNS_test_input.txt", "r")

N = int(input())
list_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dict_num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
for index in range(1, N + 1):
    temp, num = input().split()
    num = int(num)
    listx = list(input().split())

    out_num = [0]*10

    for i in range(num):
        out_num[dict_num[listx[i]]] += 1

    print(f"#{index}")
    for i in range(10):
        c = (list_num[i] + ' ') * out_num[i]
        print(c)