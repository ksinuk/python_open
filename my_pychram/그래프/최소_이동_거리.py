import sys
sys.stdin = open("최소_이동_거리.txt", "r")
#-----------------------------------------


#-----------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    nodes , num = map(int,input().split())
    lines = [0 for i in range(num)]
    table = [[(1<<31-1)*2+1 for i in range(nodes+1)] for i in range(nodes+1)]
    for i in range(num):
        a,b,c = map(int,input().split())
        lines[i] = [a,b,c]
        table[a][b] = c
    #----------------------------------------------------
    dist = [0 for i in range(nodes+1)]
    for i in range(nodes+1):
        dist[i] = table[0][i]
    
    visit = [0 for i in range(nodes+1)]
    visit[0] = 1

    while visit[nodes]==0:
        min_d = 1<<31
        mini = -1
        for i in range(nodes+1):
            if min_d > dist[i] and visit[i]==0:
                min_d = dist[i]
                mini = i
        
        visit[mini] = 1
        for i in range(nodes+1):
            dist[i] = min(dist[i],dist[mini]+table[mini][i])

    #-----------------------------------------------------
    print("#{} {}".format(test_case,dist[nodes]))