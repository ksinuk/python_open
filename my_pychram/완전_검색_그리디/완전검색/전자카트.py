import sys
sys.stdin = open("전자카트_input.txt","r")

def search(size,now,sums,mini,table,arr):
    if sums>=mini: return mini
    
    if size-1==now:
        sums = sums+table[arr[now-1]][arr[now]]
        return sums if sums < mini else mini

    for i in range(now,size-1):
        arr[now] , arr[i] = arr[i] , arr[now]
        pre = table[arr[now-1]][arr[now]]
        mini = search(size,now+1,sums+pre,mini,table,arr)
        arr[now] , arr[i] = arr[i] , arr[now]
    
    return mini


def cal_main(size):
    table = [[] for i in range(size)]
    for i in range(size):
        table[i] = list(map(int,input().split()))
    #----------------------------------------------
    mini = 0
    for i in range(size-1):
        mini += table[i][i+1]
    mini += table[size-1][0]
    #----------------------------------------------
    arr = [i for i in range(size)]
    arr.append(0)
    mini = search(size+1,1,0,mini,table,arr)

    return mini

#-----------------------------
N = int(input())
for i in range(N):
    size = int(input())
    print("#{} {}".format(i+1,cal_main(size)))