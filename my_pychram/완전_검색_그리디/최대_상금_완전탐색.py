import sys
sys.stdin = open("최대_상금_input_test.txt","r")
#-------------------------------------------
memo = {}

def search(time,now,out,cards,size,two,maxnum,memo):
    num = int(''.join(cards))
    key = now*1000000+num
    if key in memo:
        value = memo[key]
        memo[key] = out if out>value else value
        return memo[key]
    if maxnum==out or two and num == maxnum :   
        memo[key] = maxnum
        return maxnum
    if time==now:
        out = num if num>out else out
        memo[key] = out
        return out
    
    for i in range(size):
        for j in range(i+1,size):
            if cards[i]==cards[j]:continue
            temp1 = int(''.join(cards))
            cards[i] , cards[j] = cards[j] , cards[i]
            temp2 = int(''.join(cards))
            if two==0 or temp1<temp2:
                out = search(time,now+1,out,cards,size,two,maxnum,memo)
            cards[i] , cards[j] = cards[j] , cards[i]

    memo[key] = out
    return out
#-------------------------------------------
def cal_main(li,testcase = 0):
    cards , time = list(li[0]) , int(li[1])
    cards = list(cards)
    size = len(cards)
    del li
    #-------------------------------------------
    maxs = cards[:]
    maxs.sort(reverse=True)
    maxnum = int(''.join(maxs))
    
    two = 0
    for i in range(1,size):
        if maxs[i] == maxs[i-1]:
            two = 1
            break

    out = search(time,0,0,cards,size,two,maxnum,memo)
    #------------------------------------------
    return out

#-------------------------------------------
for i in range(int(input())):
    li = input().split()
    print("#{} {}".format(i+1,cal_main(li,i//9)))
    memo = {}