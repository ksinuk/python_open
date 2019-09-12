import sys
sys.stdin = open("컨테이너_운반_input.txt","r")

def sort(arr , start=0,end =-1):
    if len(arr)<2: return 0
    if end==-1:
        end = len(arr)-1
    pv = arr[(start+end)//2]
    pre = [start,end]

    while(start<=end):
        while(arr[start]<pv):start+=1
        while(arr[end]>pv):end-=1
        if start<=end:
            arr[start] , arr[end] = arr[end] , arr[start]
            start , end = start+1 , end-1

    if end>pre[0]:
        sort(arr,pre[0],end)
    if start<pre[1]:
        sort(arr,start,pre[1])
#-------------------------------------------------
def cal_main(box_num , truck_num):
    boxs = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    sort(boxs)
    sort(trucks)

    out = 0
    while len(trucks):
        truck = trucks.pop()
        while len(boxs):
            box = boxs.pop()
            if truck >= box:
                out += box
                break

    return out
#-------------------------------------------------
N = int(input())
for i in range(N):
    box_num , truck_num = map(int,input().split())
    print("#{} {}".format(i+1,cal_main(box_num , truck_num)))