import sys
sys.stdin = open("작업순서_input.txt", "r")

for test_case in range(1, 11):
    Node , line_size = map(int,input().split())
    line = list(map(int,input().split()))
 
    matrix = [[0 for i in range(Node+1)] for j in range(Node+1)]
    for i in range(0,line_size*2,2):
        matrix[line[i+1]][line[i]] = 1

    node_list = [0 for i in range(Node+1)]
    for i in range(1,Node+1):
        mat_i = matrix[i]
        temp = 0
        for j in range(1,Node+1):
            if mat_i[j]:
                temp+=1
        node_list[i] = temp

    out = [0 for i in range(Node+1)]
    out_index=0
    while out_index!=Node:
        for i in range(1,Node+1):
            if node_list[i]==0:
                for j in range(1,Node+1):
                    if matrix[j][i]:
                        node_list[j]-=1
                node_list[i]-=1
                out[out_index] = str(i)
                out_index+=1
 
    out = ' '.join(out[0:out_index])
    print(f"#{test_case} {out}")