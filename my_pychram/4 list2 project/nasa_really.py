import sys
sys.stdin = open("input.txt", "r")

def fact(n):
    out=1
    for i in range(n):
        out*=(i+1)
    return out

def make_line(now , list_nasa , index_list , list_out):
    list_next = [0]*num
    for i in range(num):
        if list_nasa[now][1] ==list_nasa[i][0] and index_list[i]==0:
            list_next[i] = 1

    len_out = 0
    for i in list_out:
        len_out+=1

    for i in range(num):
        if list_next[i]==0:
            continue

        list_out[len_out] = list_nasa[i][:]

        index_list[i]=1
        make_line(i,list_nasa,index_list , list_out)
        index_list[i]=0




    return 0
    
#-------------------------------

N = int(input())
for index in range(1,N+1):
    num = int(input())
    list_in = list(map(int,input().split()))
    list_nasa = [[0,0] for i in range(num)]
    for i in range(num):
        list_nasa[i][0] = list_in[2*i]
        list_nasa[i][1] = list_in[2*i+1]
    del list_in
    list_out = [[0, 0] for i in range(num)]
    out_len = 0
    # 입력 완료-------------------------------------
    

    

    # 출력 완료------------------------------------
    print(f"#{index} out_len:{out_len} , ",end='')
    for i in range(out_len):
        print(f" {list_out[i][0]}",end='')
        print(f" {list_out[i][1]}", end='')
    print()