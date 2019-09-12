def iswall(x,y,lenx,leny):
    out = [1,1,1,1]
    if x==0:
        out[2]=0
    if y==0:
        out[0] = 0
    if x==lenx-1:
        out[3]=0
    if y==leny-1:
        out[1]=0
    return out

arr = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
out = [[0]*5 for i in range(5)]


dx = [0,0,-1,1]
dy = [-1,1,0,0]

lenx = 5
leny = 5

for y in range(leny):
    for x in range(lenx):
        sum=arr[y][x]
        for i in range(4):
            outi = iswall(x,y,lenx,leny)
            if outi[i]==0:
                continue
            testx = x+dx[i]
            testy = y+dy[i]
            sum += arr[testy][testx]
        out[y][x]=sum

print("----------------------")
for li in out:
    print(li)
