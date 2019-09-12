import sys
sys.stdin = open("이진_힙_input.txt","r")

Testcase = int(input())
for test_case in range(1,Testcase+1):
    size = int(input())
    nums = list(map(int,input().split()))
    table = [0]*(size+1)

    for i in range(1,size+1): # 이진 힙 생성
        table[i] = nums[i-1]
        now = i
        while table[now//2] > table[now] and now>1:
            table[now//2] , table[now] = table[now] , table[now//2]
            now = now//2

    out = 0 # 조상 값들의 함 계산
    now = size//2
    while now>0:
        out += table[now]
        now = now//2

    print("#{} {} ".format(test_case,out))