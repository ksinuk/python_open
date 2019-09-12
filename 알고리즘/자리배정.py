import sys
sys.stdin = open("자리배정_input.txt", "r")

N = int(input())
for __ in range(N):
    size_x , size_y = map(int,input().split())
    x,y = 0,0
    man = int(input())
    if man > size_x*size_y:
        print('0')
        continue

    while size_x > 2 and size_y > 2:
        cut = size_x*2+(size_y-2)*2
        if man > cut:
            man -= cut
            size_x , size_y = size_x-2 , size_y-2
            x , y = x+1 , y+1
        else:
            break

    cut = size_x*2+(size_y-2)*2
    if man <= size_y:
        y += man
        x += 1
    elif man <= size_y + size_x -1:
        y += size_y
        x += man-(size_y)+1
    elif man <= 2*size_y + size_x -2:
        y += size_y - (man-(size_y + size_x -1))
        x += size_x
    else:
        y += 1
        x += size_x*2+(size_y-2)*2 - man +2
    
    print(f"{x} {y}")

    


            
    
    
