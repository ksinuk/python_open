import sys
sys.stdin = open("베이비진_게임_input.txt","r")
#-----------------------------
def babygin(arr):
    if len(arr)<3: return False

    arr.sort()
    for i in range(len(arr)-2):
        if arr[i]==arr[i+2]:
            return True 
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            if arr[i]+1==arr[j]:
                for k in range(j+1,len(arr)):
                    if arr[j]+1==arr[k]:
                        return True

    return False
#-----------------------------
def cal_main(cards_in):
    deck = [[],[]]

    for time in range(12):
        deck[time%2].append(cards_in.pop(0))
        if babygin(deck[time%2]):
            return time%2+1

    return 0
#-----------------------------
N = int(input())
for i in range(N):
    cards_in = list(map(int,input().split()))
    print("#{} {}".format(i+1,cal_main(cards_in)))