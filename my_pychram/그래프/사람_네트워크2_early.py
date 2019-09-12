import sys

sys.stdin = open("사람_네트워크2.txt", "r")
#-----------------------------------------


#-----------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    input_data = list(map(int,input().split()))
    size = input_data[0]
    table = [[-1 for i in range(size)] for j in range(size)]
    for y in range(size):
        for x in range(size):
            if(input_data[y*size+x+1]):
                table[y][x] = 1
    #del input_data
    #----------------------------------------------------
    for start in range(size):
        for dist in range(1,size):
            other = 0
            for i in range(size):
                if table[start][i]==dist:
                    for j in range(start+1,size):
                        if table[i][j]==1 and table[start][j]<0:
                            table[j][start] = table[start][j] = dist+1
                else:
                    other+=1
            if other==size:
                break
 
    outs = [0 for i in range(size)]
    for i in range(size):
        for j in range(size):
            if table[i][j]>0:
                outs[i] += table[i][j]
 
    out = min(outs)
    #-----------------------------------------------------
    print("#{} {}".format(test_case,out))



