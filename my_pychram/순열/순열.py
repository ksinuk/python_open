def myprint(q,T):
    while q!=0:
        q=q-1
        print(" {} ".format(T[q]),end="")
    print()

def perm(n,r,q,t,a):
    if r==0:
        myprint(q,t)
    else:
        for i in range(n-1,-1,-1):
            a[i] , a[n-1] = a[n-1] , a[i]
            t[r-1] = a[n-1]
            perm(n-1,r-1,q,t,a)
            a[i] , a[n-1] = a[n-1] , a[i]

def pi(n,r,q,t,a):
    if r==0:
        myprint(q,t)
    else:
        for i in range(n-1,-1,-1):
            t[r-1] = a[i]
            pi(n,r-1,q,t,a)

a = [1,2,3,4]
t = [0]*3
perm(4,3,3,t,a)
print("---------")
pi(4,3,3,t,a)