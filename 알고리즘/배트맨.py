import sys
sys.stdin = open("배트맨.txt","r")
#---------------------------------
def cal_main(size):
    arr = list(map(int,input().split()))

    out = 0
    height = arr[0]
    time = 1
    while time<size:
        height-=1
        if arr[time]>height:
            out+=1
            height = arr[time]
            time+=1
        else:
            if(time+1<size):
                height = arr[time+1]
            time+=2

    return out

#---------------------------------
N = int(input())
for i in range(N):
    size = int(input())
    print(cal_main(size))