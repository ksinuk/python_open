import sys
sys.stdin = open("그래프경로_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    Node , num = map(int,input().split()) # 노드 , 경로의 갯수
    lines = [[0,0] for i in range(num)] # 경로 모음
    out=0 # 출력값
    
    for i in range(num): #경로 입력 받기
        a , b = map(int,input().split())
        if a==b: #자기 자신을 가리키는 노드 제거
            break
        lines[i][0] = a
        lines[i][1] = b
        
    matrix = [ [0 for i in range(Node)] for i in range(Node)] # 경로 표
    for line in lines:
        matrix[line[0]-1][line[1]-1] = 1
    
    start , end = map(int,input().split()) # 시작점과 종료점
    start , end = start-1 , end-1
    #------------------------------------------
    ok_node = [0]*(Node) # 이미 지나갔거나 지나갈 예정인 노드 모음
    ok_node[start] = 1
    stack = [0]*(Node*2) # 검색할 노드 모음
    index=-1
    now = start # 검사하고 있는 노드
    
    while out==0:
        mat_now = matrix[now] # 시작점인 now의 노드의 종료점 모음
        for endpoint in range(Node):
            if mat_now[endpoint]==0: # 종료점이 아님
                continue
            if endpoint==end: # 종료점 발견 , 종료점 발견시 루프 종료
                out=1
                break
            elif ok_node[endpoint]==0: # 지나가도록 설정
                ok_node[endpoint] = 1
                index+=1
                stack[index] = endpoint

        if index<0: # 더이상 검색할 노드가 없음
            break
        now = stack[index] #다음 노드 설정
        index-=1

    print(f"#{test_case} {out}")