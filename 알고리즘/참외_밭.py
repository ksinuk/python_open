import sys
sys.stdin = open("참외_밭.txt","r")

for __ in range(3):
    base = int(input())
    inline = [[] for i in range(6)]
    size_y = 0
    size_x = 0
    for i in range(6):
        inline[i] = list(map(int,input().split()))
        if inline[i][0] < 3 and size_x<inline[i][1]:
            size_x = inline[i][1]
        elif inline[i][0] >= 3 and size_y<inline[i][1]:
            size_y = inline[i][1]

    inx = 0
    iny = 0   
    for i in range(6):
        if inline[(6+i-1)%6][0] == inline[(6+i+1)%6][0]:
            if inline[i][0] < 3:
                inx = inline[i][1]
            else:
                iny = inline[i][1]
    
    out = base*(size_y*size_x -iny*inx)
    print(out)


