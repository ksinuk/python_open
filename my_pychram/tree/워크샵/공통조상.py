import sys
sys.stdin = open("공통조상_input.txt","r")

Testcase = int(input())
for test_case in range(1,Testcase+1):
    size , line_size , x1,x2 = map(int,input().split())
    inline = list(map(int,input().split()))

    table = [0]*(size+1)

    for i in range(0,line_size*2,2):
        a ,b = inline[i] , inline[i+1]
        if table[a]==0:
            table[a] = [b,0,0]
        elif table[a][0]==0:
            table[a][0] = b
        else:
            table[a][1] = b

        if table[b] == 0:
            table[b] = [0, 0, a]
        else:
            table[b][2] = a
    del inline
    # 입력 완료 -----------------------------------------------
    history1 = [0]*size
    history1[0] = x1
    index1 = 0
    history2 = [0]*size
    history2[0] = x2
    index2 = 0

    while 1:
        now = history1[index1]
        index1 +=1
        if table[now][2]:
            history1[index1] = table[now][2]
        else:
            break
    while 1:
        now = history2[index2]
        index2 +=1
        if table[now][2]:
            history2[index2] = table[now][2]
        else:
            break

    same = 0
    for node in history1:
        if node in history2:
            same = node
            break

    del history1
    del history2

    out = 0
    qu = [0]*(size+1)
    qu[0] = same
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

    print("#{} {} {}".format(test_case,same,out))