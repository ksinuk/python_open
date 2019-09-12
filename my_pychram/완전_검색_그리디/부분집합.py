cnt = 0
N = 3
A = [0 for i in range(N)]
data = [i+1 for i in range(N)]

def printset(n):
    global cnt
    cnt+=1
    print(f"{cnt} : ",end='')
    for i in range(n):
        if A[i]:
            print(f"{data[i]} ",end='')
    print()

def powerset(n,k):
    if n==k:printset(n)
    else:
        A[k] = 1
        powerset(n,k+1)
        A[k] = 0
        powerset(n,k+1)

powerset(N,0)
