import sys
sys.stdin = open("비밀금고.txt","r")

for __ in range(1):
    size = int(input())
    size = size*2-1
    inline = list(map(int,input().split()))

    maps = [[0 for i in range(size)] for j in range(size)]
    x , y = 0 ,(size+1)//2-1
    cut = (size+1)//2-1
    cnt = 1
    for i in range(len(inline)):
        num = inline[i]
        maps[y][x] = num
        cnt-=1
        y-=2
        if cnt==0:
            x+=1
            cnt = x+1 if x<cut else cut+1-(x-cut)
            y = cut+x if x<cut else 2*cut-(x-cut)
                      
    
    max_out = sum(maps[0])
    for y in range(1,size):
        temp = sum(maps[y])
        if temp > max_out:
            max_out = temp
    
    print(max_out)




