import sys
sys.stdin = open("화물_도크_input.txt","r")
#----------------------------
def sort(arr):
    if len(arr)<2: return 0
    size = len(arr)
    step = 1
    now = 0

    while(step<size):
        qu = []
        a , ar = now , now+step
        b , br = now+step , now+step*2
        br = size if size < br else br

        while(a<ar and b<br):
            if(arr[a][0]<arr[b][0] or arr[a][0]==arr[b][0] and arr[a][1]>arr[b][1]):
                qu.append(arr[a])
                a+=1
            else:
                qu.append(arr[b])
                b+=1
        while(a<ar):
            qu.append(arr[a])
            a+=1
        while(b<br):
            qu.append(arr[b])
            b+=1
        
        i = now
        while(qu):
            arr[i] = qu.pop(0)
            i+=1

        now += step*2
        if(now+step>=size):
            now = 0
            step*=2
#-----------------------------
def cal_main(size):
    table = []
    for i in range(size):
        a,b = map(int,input().split())
        table.append([a,b])
    sort(table)
    #-----------------------------------
    i= 0
    while i<size:
        for j in range(i+1,size):
            if table[i][0] <= table[j][0] and table[i][1] >= table[j][1]:
                break
        else:
            i+=1
            continue
        table.pop(i)
        size-=1

    #------------------------------------
    out = 0
    check = 0
    index = 0
    last = [0]*size
    history = [0]*size
    while(index>=0):
        if index==size or index!=0 and history[index-1]+size-index <= out:
            out = history[size-1] if history[size-1]>out else out
            check//=2
            index-=1
            check+=1
            while(check%2==0):
                check//=2
                index-=1
        else:
            if index!=0:
                history[index] = history[index-1]
                last[index] = last[index-1]
            else:
                history[index] = 0
                last[index] = 0

            if check%2==0 and last[index]<=table[index][0]:
                history[index]+=1
                last[index] = table[index][1]

            index+=1
            check*=2
            
    return out
#-----------------------------
N = int(input())
for i in range(N):
    size = int(input())
    print("#{} {}".format(i+1,cal_main(size)))

