import sys
sys.stdin = open("card_game_input.txt", "r")

def game(a,b):
    if a==b:
        return 0
    if a == 1 and b == 2:
        return 1
    if a == 1 and b == 3:
        return -1
    if a == 2 and b == 1:
        return -1
    if a == 2 and b == 3:
        return 1
    if a == 3 and b == 1:
        return 1
    if a == 3 and b == 2:
        return -1


def winner(lists,left,right):
    if right==left:
        return right
    elif right-left==1:
        result = game(lists[left] , lists[right])
        if result==1:return right
        else: return left

    temp_left = winner(lists,left,(left+right)//2)
    temp_right = winner(lists, (left+right)//2+1, right)
    result = game(lists[temp_left], lists[temp_right])
    if result == 1: return temp_right
    else: return temp_left

    return 0

T = int(input())
for test_case in range(1, T + 1):
    man = int(input())
    lists = list(map(int , input().split()))

    out = winner(lists,0,man-1)

    print(f"#{test_case} {out+1}")