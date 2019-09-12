import sys
sys.stdin = open("subtree_input.txt","r")

Testcase = int(input())
for test_case in range(1,Testcase+1):
    size , x = map(int,input().split())
    size+=1
    inline = list(map(int,input().split()))

    table = [0]*(size+1)

    for i in range(0,len(inline),2): # 트리 생성
        a ,b = inline[i] , inline[i+1]
        if table[a]==0: table[a] = [b,0,0]
        elif table[a][0]==0: table[a][0] = b
        else: table[a][1] = b

        if table[b] == 0: table[b] = [0, 0, a]
        else: table[b][2] = a
    del inline
    # 입력 완료 -----------------------------------------------
    out = 0 # 노드의 개수
    qu = [0]*(size+1) # 큐
    qu[0] = x
    start = 0
    end = 0
    while start<=end:
        now = qu[start] ; start+=1
        now = table[now]
        if now[0]:
            qu[end+1] = now[0] ; end+=1
        if now[1]:
            qu[end+1] = now[1] ; end+=1
    out = end+1

    print("#{} {}".format(test_case,out))