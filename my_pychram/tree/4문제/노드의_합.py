import sys
sys.stdin = open("노드의_합_input.txt","r")

def cal(table,i): # postorder
    if i<1 or i>=len(table) or table[i]:
        return 0
    cal(table, i*2)
    cal(table, i*2+1)
    if i*2+1<len(table):
        table[i] = table[i*2]+table[i*2+1]
    elif i*2<len(table):
        table[i] = table[i*2]


T = int(input())
for test_case in range(1, T + 1):
    size , line_size , x = map(int,input().split())
    table = [0]*(size+1)

    for i in range(line_size):# 트리 생성
        a,b = map(int,input().split())
        table[a] = b
    # 입력 완료 --------------------------------------
    cal(table,1)

    print("#{} {}".format(test_case,table[x]))