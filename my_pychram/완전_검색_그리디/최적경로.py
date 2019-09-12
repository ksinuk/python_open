import sys
sys.stdin = open("최적경로_input.txt","r")
table = []
arr = []
min_d = []

def maketable(size):
    global table , min_d
    tables = [[0,0] for i in range(size)]
    li = list(map(int,input().split()))
    for i in range(0,size):
        tables[i] = [li[i*2],li[1+i*2]]
    
    tables[1] , tables[size-1] = tables[size-1] , tables[1]

    for i in range(size):
        for j in range(i+1,size):
            temp = abs(tables[i][0]-tables[j][0])+abs(tables[i][1]-tables[j][1])
            table[i][j] = table[j][i] = temp

    for i in range(size):
        minnum = 1<<30
        for j in range(size):
            if minnum > table[i][j] and i!=j:
                minnum = table[i][j]
        min_d.append(minnum)

def search(sizem1,now,sums,mins):
    if sizem1==now:
        sums+= table[now][arr[now-1]]
        return sums if sums<mins else mins

    last_min = 0
    for i in range(now,sizem1):
        last_min += min_d[i]
    if sums+last_min >= mins:return mins

    next_arr = arr[now:sizem1]
    for i in range(0,len(next_arr)-1):
        min_i = i
        for j in range(i+1,len(next_arr)):
            if table[next_arr[min_i]][arr[now-1]] > table[next_arr[j]][arr[now-1]]:
                min_i = j
        next_arr[i] , next_arr[min_i] = next_arr[min_i] , next_arr[i]

    for i in next_arr:
        x =0
        for j in range(now,sizem1):
            if arr[j]==i:
                x=j
                break
        arr[now],arr[x] = arr[x],arr[now]
        now_sum = sums + table[arr[now]][arr[now-1]]
        if(now_sum<mins):
            mins = search(sizem1,now+1,now_sum,mins)
        arr[now],arr[x] = arr[x],arr[now]

    return mins

def cal_main(size):
    global table,arr
    size+=2
    table = [[0 for j in range(size)] for i in range(size)]
    maketable(size)
    #---------------------------------------
    mins = 0
    for i in range(1,size):
        mins += table[i][i-1]

    arr = [i for i in range(size)]
    mins = search(size-1,1,0,mins)

    return mins

#-------------------------------------------
N = int(input())
for i in range(N):
    size = int(input())
    print("#{} {}".format(i+1,cal_main(size)))
    table = []
    arr = []
    min_d = []