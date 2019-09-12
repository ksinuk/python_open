import sys
sys.stdin = open("최대_상금_input.txt","r")
#-------------------------------------------
def cal_main(li):
    cards , time = list(li[0]) , int(li[1])
    cards = list(map(int,cards))
    size = len(cards)
    del li
    #-------------------------------------------
    maxs = cards[:]
    maxs.sort(reverse=True)
    #-------------------------------------------
    start = 0
    while time>0 and maxs:
        max1 = maxs.pop(0)
        cnt = 1
        while maxs and maxs[0]==max1:
            maxs.pop(0)
            cnt+=1
        
        start += cnt
        for i in range(start):
            if cards[i]==max1:
                cnt-=1
        if cnt<=0:continue

        others = []
        for i in range(size):
            if cards[i]<max1:
                others.append(cards[i])
                cards[i] = max1
                if len(others)>=cnt:
                    break
        if not(others):continue
        others.sort(reverse=True)
        
        for i in range(size-1,start-1,-1):
            if cards[i] == max1:
                cards[i] = others.pop()
                time-=1
                if len(others)==0:
                    break
    #---------------------------------------
    if time<=0 or time%2==0:
        cards = ''.join(map(str,cards))
        return int(cards)
    for i in range(size):
        for j in range(i+1,size):
            if cards[i]==cards[j]:
                cards = ''.join(map(str,cards))
                return int(cards)
    #----------------------------------------
    cards[size-1] , cards[size-2] = cards[size-2] , cards[size-1]

    cards = ''.join(map(str,cards))
    return int(cards)

#-------------------------------------------
for i in range(int(input())):
    li = input().split()
    print("#{} {}".format(i+1,cal_main(li)))

