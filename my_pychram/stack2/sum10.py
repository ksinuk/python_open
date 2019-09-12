def sum10(li):
    out = 0
    for p in li:
        out += num[p]
    return out

def print_out(li):
    out = li[:]
    for i in range(len(li)):
        out[i] = num[li[i]]
    print(out)
#-----------------------------------------
num = [10,9,8,7,6,5,4,3,2,1]
num.sort()
num = num[::-1]
stack_p = [0 for i in range(10)]
size_p = 0

stack_p[size_p] = 0; size_p+=1

cnt = 0
while size_p:
    cnt+=1
    sum_now = sum10(stack_p[0:size_p])
    if sum_now>=10:
        if sum_now == 10: print_out(stack_p[0:size_p])
        if stack_p[size_p - 1] == 9:
            size_p -=1
            if size_p==0:break
        stack_p[size_p - 1] += 1

    else:
        if stack_p[size_p - 1] == 9:
            size_p -=1
            if size_p==0:break
            stack_p[size_p - 1]+=1
        else:
            stack_p[size_p] = stack_p[size_p - 1] + 1
            size_p+=1

print(f"cnt : {cnt}")







