import sys
sys.stdin = open("이진탐색_input.txt","r")

def cal(table,now,nums): # inorder
    if now >= len(table) or now<1:
        return 0
    cal(table,now*2,nums)
    table[now] = nums[0]
    nums[0]+=1
    cal(table, now*2+1, nums)

Testcase = int(input())
for test_case in range(1,Testcase+1):
    num = int(input())
    table = [0]*(num+1)

    cal(table, 1 ,[1])

    print("#{} {} {}".format(test_case,table[1],table[num//2]))