import sys
sys.stdin = open("node_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    node_size , line_size = map(int , input().split()) # 노드의 종류 , 라인의 갯수

    table=[[0 for i in range(node_size+1)] for i in range(node_size+1)] # 노드 연결 테이블
    for i in range(line_size):
        a , b = map(int , input().split())
        if a==b:break
        table[a][b] = 1
        table[b][a] = 1

    start , end = map(int , input().split()) # 시작점과 중단점
    out = 0 # 결과값
    qu = [0 for i in range(node_size+10)] # 큐
    qu[0] = start #큐에 시작점 입력
    qu_in = 1 # 큐에서 입력 받아야 할 지점
    qu_out = 0 # 큐에서 출력해야 할 지점
    ok = 0 # 도착점 찾을 경우 1 , 그 외에는 0

    # 입력 완료 -------------------------------
    while start!=end and qu_in!=qu_out:
        out += 1
        cut = qu_in
        for qu_i in range(qu_out,cut): # 다음 노드 찾기
            now = qu[qu_i] # 라인의 시작점

            for i in range(1,node_size+1):
                if table[now][i]: # 라인의 종료점 발견
                    if i==end: # 도착점 발견
                        ok=1
                        break
                    qu[qu_in] = i;qu_in+=1 # 다음 노드 큐에 입력
                    table[now][i] = 0 # 테이블에서 라인 제거
                    table[i][now] = 0
            if ok:break 
        qu_out = cut # 다음 노드 검색      
        if ok:break 

    if ok:
        print(f"#{test_case} {out}")
    else:
        print(f"#{test_case} 0")