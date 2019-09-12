import sys
sys.stdin = open("최소합_input.txt","r")

def cal_main(size):
    table = [[] for i in range(size)]
    for i in range(size):
        table[i] = list(map(int,input().split()))
    #---------------------------------------------
    mini = 0
    for x in range(size): mini += table[0][x]
    for y in range(1,size): mini += table[y][size-1]
    #------------------------------------------------
    len_arr = size*2-1
    sums = [0 for i in range(len_arr)]
    check = 0
    index = 0
    points = [[0,0] for i in range(len_arr)]

    while(index>=0):
        x,y= points[index][1] , points[index][0]
        sums[index] = table[y][x]
        if index != 0: 
            sums[index] += sums[index-1]
        #-----------------------------------------------
        if index == len_arr-1 or sums[index] >= mini:
            mini = sums[index] if sums[index] < mini else mini

            if points[index][0]==size-1:
                while check%2==0 and index>=0:
                    check//=2
                    index-=1
            if index<0: break

            check+=1
            while check%2==0:
                check//=2
                index-=1
            if index<0: break

            index+=1
            check *=2
            points[index][0] , points[index][1] = points[index-1][0]+1 , points[index-1][1]

        else:
            index+=1
            if points[index-1][1] == size-1:
                check = 2*check+1
                points[index][0] , points[index][1] = points[index-1][0]+1 , points[index-1][1]
            else:
                check *=2
                points[index][0] , points[index][1] = points[index-1][0] , points[index-1][1]+1

    return mini
#------------------------
N = int(input())
for i in range(N):
    size = int(input())
    print("#{} {}".format(i+1,cal_main(size)))