import sys
sys.stdin = open("연속부분최대곱.txt", "r")

size = int(input())
nums = [0]*size
for i in range(size):
    nums[i] = float(input())

max_num = max(nums)
# 입력 완료 , 연산시작 ----------------
while size>1:
    if nums[size-1] < 1:
        size-=1
    else:
        break   

i=0
while size-i>1:
    if nums[i] < 1:
        i+=1
    elif nums[i+1]>1:
        nums[i+1] *= nums[i]
        i+=1
        if nums[i] > max_num:
            max_num = nums[i]
    else:
        nums[i+1] *= nums[i]
        i+=1

print("{:.3f}".format(max_num))




