import sys
sys.stdin = open("number_turn_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size , time = map(int , input().split())
    nums = list(map(int , input().split()))
    index = 0
    
    for i in range(time):
        index = (index+1)%size
    
    print(f"#{test_case} {nums[index]}")