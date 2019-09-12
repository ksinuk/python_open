def myprint(q):
    for i in range(q):
        print(" {} ".format(T[i]),end="")
    print()
def comb(n,r,q,T,A):
    if r==0:
        myprint(q)
    elif n<r:
        return
    else:
        comb(n-1,r,q,T,A)
        T[r-1] = A[n-1]
        comb(n-1,r-1,q,T,A)

def Hcomb(n,r,q,T,A):
    if r==0:
        myprint(q)
    elif n==0:
        return
    else:
        T[r-1] = A[n-1]
        Hcomb(n,r-1,q,T,A)
        Hcomb(n-1,r,q,T,A)
        

def mycomb(n,r,T,A,H=0):
    H=(H+1)%2
    point = [i*H for i in range(r)]
    
    index=0
    while index>=0:
        if index==r:
            myprint(r)
            index-=1
        elif point[index]+(r-1-index)*H >= n:
            index-=1
            for ii in range(index,r-1):
                point[ii+1] = point[ii]+H
        else:
            T[index] = A[point[index]]
            point[index]+=1
            index+=1
        
def comb_cal(n,r):  
    memo = [[0 for i in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,r)+1):
            if j==0 or j==i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i-1][j-1]+memo[i-1][j]

    return memo[n][r]

n,r=4,3
A=[1,2,3,4]

T=[0]*3
comb(n,r,r,T,A)
print("-------------------")
T=[0]*3
mycomb(n,r,T,A)
print("-------------------")
T=[0]*3
Hcomb(n,r,r,T,A)
print("-------------------")
T=[0]*3
mycomb(n,r,T,A,1)

    