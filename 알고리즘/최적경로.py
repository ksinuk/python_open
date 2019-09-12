import sys
sys.stdin = open("최적경로_input.txt","r")
table = []
arr = []

def maketable(size):
    global table
    tables = [[0,0] for i in range(size)]
    li = list(map(int,input().split()))
    for i in range(0,size*2,2):
        tables[i] = [li[i],li[1+i]]
    
    tables[1] , tables[size-1] = tables[size-1] , tables[1]

    for i in range(size):
        for j in range(i+1,size):
            temp = abs(tables[i][0]-tables[j][0])+abs(tables[i][1]-tables[j][1])
            table[i][j] = table[j][i] = temp

def search(sizem1,now,sums,mins):
    if sums>=mins:
        return mins
    if sizem1==now:
        sums+= table[now][arr[now-1]]
        return sums if sums<mins else mins

    for i in range(now,sizem1):
        arr[now],arr[i] = arr[i],arr[now]
        now_sum = sums + table[arr[now]][arr[now-1]]
        mins = search(sizem1,now+1,now_sum,mins)
        arr[now],arr[i] = arr[i],arr[now]

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