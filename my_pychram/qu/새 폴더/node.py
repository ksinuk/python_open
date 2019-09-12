import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    node_size , start = map(int , input().split()) # 노드의 갯수 , 시작 지점

    table=[[0 for i in range(node_size+1)] for j in range(node_size+1)] # 방향 테이블
    line_temp = list(map(int,input().split())) # 라인 목록
    for i in range(0,len(line_temp),2): # 방향 테이블 작성
        a , b = line_temp[i] , line_temp[i+1]
        if a==b:continue
        table[a][b] = 1 

    qu = [[-1,-1] for i in range(node_size+10)] # 확인한 노드를 저장하는 큐
    qu[0] = [start,0] # 시작 지점 입력
    qu_end = 0 # 마지막 노드의 위치
    qu_start = 0 # 탐색하지 못한 노드의 첫번째 위치
    # 입력 완료 -------------------------------
    while qu_start <= qu_end: # 탐색 할 노드가 있으면 탐색
        nows = qu[qu_start] ; qu_start+=1 # 시작 지점 출력
        node , distence = nows[0] , nows[1] # 시작 지점의 노드와 첫 노드 사이의 거리
        for i in range(1,node_size+1):
            if table[node][i]: # 다음 노드 발견 
                qu[qu_end+1] = [i,distence+1] ; qu_end+=1
                table[node][i] = 0
            table[i][node] = 0
    
    out_max = qu[qu_end][1] # 거리가 가장 먼 노드 중에서 값이 가장 큰 노드 찾기
    out = qu[qu_end][0]
    for i in range(qu_end,-1,-1):
        nows = qu[i]
        if out_max != nows[1]:break
        out = nows[0] if nows[0] > out else out


    print(f"#{test_case} {out}")
    
    
    
    
    