import sys
sys.stdin = open("수열.txt","r")

for __ in range(3):
    size = int(input())
    li1 = list(map(int , input().split() ))
    li2 = li1[::-1]
    
    out1 = 0
    now = 0
    for i in range(size-1):
        if li1[i] > li1[i+1]:
            out1 = now if now>out1 else out1
            now = 0
        else:
            now+=1
    out1 = now if now>out1 else out1

    out2 = 0
    now = 0
    for i in range(size-1):
        if li2[i] > li2[i+1]:
            out2 = now if now>out2 else out2
            now = 0
        else:
            now+=1
    out2 = now if now>out2 else out2

    out = out1 if out1>out2 else out2
    print(out+1)
    
            