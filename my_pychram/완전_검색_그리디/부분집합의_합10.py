def to10(cut,arr,size,check,now,sums,cnt):
    if sums==cut:
        cnt+=1
        print("{} : ".format(cnt),end="")
        for i in range(now):
            if check[i]: print("{} ".format(arr[i]),end="")
        print()
        return cnt
    if sums>cut:
        return cnt
    if size==now:
        return cnt

    check[now] = 1
    cnt = to10(cut,arr,size,check,now+1,sums+arr[now],cnt)
    check[now] = 0
    cnt = to10(cut,arr,size,check,now+1,sums,cnt)

    return cnt


size = 10
arr = [1,2,3,4,5,6,7,8,9,10]
check = [0 for i in range(size)]

to10(10,arr,size,check,0,0,0)