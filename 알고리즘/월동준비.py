import sys
sys.stdin = open("mouse_input.txt", "r")

size = int(input())
nums = list(map(int , input().split()))
perfact = 0
ok = 0
for i in range(size):
    if nums[i] > 0:
        ok=1
        perfact += nums[i]

max_num = max(nums)
if ok==0:
    perfact = max_num 
# 입력 완료 , 연산시작 ----------------
while size>1:
    if nums[size-1] < 0:
        size-=1
    else:
        break   

i=0
while size-i>1:
    if nums[i] < 0:
        i+=1
    elif nums[i+1]>0:
        nums[i+1] += nums[i]
        i+=1
        if nums[i] > max_num:
            max_num = nums[i]
    else:
        nums[i+1] += nums[i]
        i+=1

print(f"{max_num} {perfact}")
