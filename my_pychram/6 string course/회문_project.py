import sys
import time
sys.stdin = open("회문_project_input.txt", "r")

def palindrome(strx , start , end):
    if end+1 == start:
        return 2

    lenx = (end - start + 1)
    for i in range(lenx // 2):
        if strx[start + i] != strx[end - i]:
            return 0
    return lenx + 2

def transposed_matrix(mat, out):
    for y in range(100):
        for x in range(y, 100):
            out[y][x], out[x][y] = mat[x][y], mat[y][x]

def search(table, out=1):
    start_x = 0
    if out == 100:
        return 100

    while start_x <= 99 - out:
        for y in range(100):
            text_y = table[y]
            for end_x in range(99, start_x + out - 1, -1):
                if text_y[start_x] == text_y[end_x]:
                    temp = palindrome(text_y, start_x + 1, end_x - 1)
                    if out < temp:
                        out = temp
                    if temp:
                        break
            if start_x > 99 - out:
                return out
        start_x += 1

    return out

for test_case in range(1, 11):
    input()

    table = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        table[i] = input()

    out = search(table)
    next_table = [[0 for _ in range(100)] for _ in range(100)]
    transposed_matrix(table, next_table)
    out = search(next_table, out)

    print(f"#{test_case} {out}")