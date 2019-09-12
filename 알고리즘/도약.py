import sys
sys.stdin = open("frog_input.txt", "r")

def search(arr,x,start,end):
    if x < arr[start]:
        return [-1,start]
    if arr[end] < x:
        return [end,-1]

    while start<=end:
        mid = (start + end)//2
        now = arr[mid]
        if now == x:
            return [mid,mid]
        elif now < x:
            start = mid
        else:
            end = mid
        if start+1 == end:
            break
    if leaf[end] == x:
        start = end
    elif leaf[start] == x:
        end = start
    return [start , end]
    

size = int(input())
leaf = [0]*size
for i in range(size):
    leaf[i] = int(input())
leaf.sort()

out = 0
for p1 in range(size-2):
    x1 = leaf[p1]
    for p2 in range(p1+1,size-1):
        x2 = leaf[p2]
        y1 , y2 = (x2-x1)+x2 , 2*(x2-x1)+x2
        out1 , out2 = p2+1 , size-1

        if y1 > leaf[out2] or y2 < leaf[out1]:continue
        elif y1 == leaf[out2] or y2 == leaf[out1]:
            out+=1
            continue

        result1 , result2 = [out1,out1] , [out2,out2]
        if leaf[out1] < y1 < leaf[out2]:
            result1 = search(leaf,y1,out1,out2)

        if leaf[out1] < y2 < leaf[out2]:
            result2 = search(leaf,y2,out1,out2)

        out += result2[0] - result1[1] +1

print(out)





