import sys
sys.stdin = open("뽑기상자.txt","r")
#---------------------------------
def sort(arr,size):
    if size<2: return 0
    
    step = 1
    now = 0

    while step<size:
        qu = [0 for i in range(step*2)]
        idx = 0
        a ,ar , b , br = now, now+step, now+step, now+step*2
        br = size if br>size else br

        while(a<ar and b<br):
            if arr[a] < arr[b]:
                qu[idx] = arr[a]
                idx , a = idx+1 , a+1
            else:
                qu[idx] = arr[b]
                idx , b = idx+1 , b+1
        while(a<ar):
            qu[idx] = arr[a]
            idx , a = idx+1 , a+1
        while(b<br):
            qu[idx] = arr[b]
            idx , b = idx+1 , b+1

        for i in range(idx):
            arr[now+i] = qu[i]
        
        now+=2*step
        if now+step>=size:
            step*=2
            now = 0
#-----------------------------------
def cal_main(size):
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))

    i = 0
    while i<size:
        j = 0
        while j<size and i<size:
            if p1[i]==p2[j]:
                p1[i] , p1[size-1] = p1[size-1] , p1[i]
                p2[j] , p2[size-1] = p2[size-1] , p2[j]
                size-=1
                j = 0
            else:
                j+=1
        i+=1

    sort(p1,size)
    sort(p2,size)
    
    i = 0
    out = 0
    while i<size:
        if p1[i] == p2[i]:
            i+=1
            continue
        elif i==size-1 or p1[i]!=p1[i+1] or p2[i]!=p2[i+1]:
            return -1
        
        out+=1
        i+=2

    return out

#---------------------------------
N = 2
#N = int(input())
for i in range(N):
    size = int(input())
    print(cal_main(size))