import sys
sys.stdin = open("장훈이의_높은_선반_input.txt","r")

def search(mans,size,now,sum_,min_,top):
    if size==now:
        return min_ 
    temp_sum = sum_+mans[now]
    if temp_sum < top:
        min_ = search(mans,size,now+1,temp_sum,min_,top)
    else:
        min_ = temp_sum if temp_sum < min_ else min_  
    min_ = search(mans,size,now+1,sum_,min_,top)

    return min_


def cal_main(size,top):
    mans = list(map(int,input().split()))
    mans.sort()
    min_ = 0
    for i in range(size):
        min_ += mans[i]
        if min_ >= top:
            break

    #min_ = search(mans,size,0,0,min_,top)
    check = 0
    index = 0
    history = [0 for i in range(size)]
    while index>=0:
        history[index] = 0 if index==0 else history[index-1] 
        if check%2==0:
            history[index] += mans[index]
        
        if history[index]<top:
            if index<size-1:
                check *=2
                index+=1
            else:
                check+=1
                while index>=0 and check%2==0:
                    check //=2
                    index-=1
                if index<0:break
        else:
            min_ = history[index] if history[index]<min_ else min_    
            check+=1
            while index>=0 and check%2==0:
                check //=2
                index-=1
            if index<0:break

    return min_

#-----------------------------------
N = int(input())
for i in range(N):
    size , top = map(int,input().split())
    print("#{} {}".format(i+1,cal_main(size,top)-top))