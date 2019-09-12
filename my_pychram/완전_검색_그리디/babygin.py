def babygin(li):
    if li[0]==li[1] and li[1]==li[2]:
        if li[3]==li[4] and li[4]==li[5]: return True
        if li[3]+1==li[4] and li[4]+1==li[5]: return True
        return False
    if li[0]+1==li[1] and li[1]+1==li[2]:
        if li[3]==li[4] and li[4]==li[5]: return True
        if li[3]+1==li[4] and li[4]+1==li[5]: return True
        return False
    
    return False

def perm(li,k):
    if k==1: return babygin(li)
    
    for i in range(k,0,-1):
        li[k] , li[i] = li[i] , li[k]
        if(perm(li,k-1)): return True
        li[k] , li[i] = li[i] , li[k]
        
    return False


arr = ['112244','124783','667767','000456','101123','112233']
for s in arr:
    li = list(map(int,list(s)))
    li.sort()
    
    if perm(li,4):
        print("YES")
    else:
        print("NO")

