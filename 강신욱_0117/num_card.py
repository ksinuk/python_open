import sys
sys.stdin = open("num_card_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    strx = input()
    listx = [0]*10
    
    for i in range(n):
        c = int(strx[i])
        listx[c]+=1
    
    max = listx[0]
    point = -1
    for i in range(10):
        if max<=listx[i]:
            max = listx[i]
            point = i

    print(f"#{test_case} {point} {max}") 