import sys
sys.stdin = open("plus_input.txt", "r")

N  = int(input())
for test in range(1,N+1):
    strx , y = input().split()
    size = len(strx)
    y = int(y)
    if size < 2 or int(strx)==0:
        print("NONE")
        continue

    temp = 0
    for i in range(len(strx)):
        if strx[i]=='0':
            temp = i+1
        else:
            break
    strx = strx[temp:size]
    size = size - temp

    ok = 0
    for i in range(1,len(strx)):
        x1 = int(strx[0:i])
        x2 = int(strx[i:size])
        if x1 > y:
            break
        elif x2 > y:
            continue
        
        if x1+x2 == y:
            ok=1
            print(f"{x1}+{x2}={y}")
            break
    
    if ok==0:
        print("NONE")

        




    
