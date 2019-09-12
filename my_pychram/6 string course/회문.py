import sys
sys.stdin = open("회문_input.txt", "r")

def palindrome(strx):
    for i in range(len(strx)//2):
        if strx[i] != strx[len(strx)-1-i]:
            return 0
    return 1

def transposed_matrix(mat,size):
    for y in range(size):
        for x in range(y,size):
            mat[y][x] , mat[x][y] = mat[x][y] , mat[y][x]

T = int(input())
for test_case in range(1, T + 1):
    len_table , len_x = map(int,input().split())

    table = [[] for i in range(len_table)]
    for i in range(len_table):
        table[i] = list(input())

    out = ''
    byebye = 0
    for yi in range(len_table):
        for xi in range(len_table - len_x + 1):
            temp = table[yi][xi:xi+len_x]
            if palindrome(table[yi][xi:xi+len_x]):
                out = table[yi][xi:xi+len_x]
                byebye = 1
                break
        if byebye:
            break

    if byebye:
        out_text = ''
        for c in out:
            out_text+=c
        print("#{} {}".format(test_case,out_text))
        continue

    transposed_matrix(table,len_table)
    for yi in range(len_table):
        for xi in range(len_table - len_x + 1):
            if palindrome(table[yi][xi:xi+len_x]):
                out = table[yi][xi:xi+len_x]
                byebye = 1
                break
        if byebye:
            break

    out_text = ''
    for c in out:
        out_text += c
    print("#{} {}".format(test_case, out_text))





