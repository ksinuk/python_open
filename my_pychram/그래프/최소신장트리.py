import sys
sys.stdin = open("최소신장트리.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    nodes,size = map(int,input().split())
    lines = [[0,0,0] for i in range(size)]
    for i in range(size):
        lines[i] = list(map(int,input().split()))
    #----------------------------------------------
    visit = [0 for i in range(nodes+1)]
    visit[lines[0][0]] = 1
    out = 0

    while 1:
        maxs = 1<<30
        point = -1
        i = 0
        while i<size:
            line = lines[i]
            if visit[line[0]] == visit[line[1]] == 1:
                lines[size-1] , lines[i] = lines[i] , lines[size-1]
                size , i = size-1,i-1
            elif visit[line[0]] != visit[line[1]] and maxs>line[2]:
                point = i
                maxs = line[2]
            i+=1
        if point == -1:
            break
        
        visit[lines[point][0]] = 1      
        visit[lines[point][1]] = 1
        out += lines[point][2]

        lines[size-1] , lines[point] = lines[point] , lines[size-1]
        size-=1
        
    print("#{} {}".format(test_case,out))