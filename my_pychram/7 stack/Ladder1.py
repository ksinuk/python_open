import sys
sys.stdin = open("Ladder1_input.txt", "r")

for testcase in range(1, 11):
    input()
    matrix = [[] for i in range(100)]
    for i in range(100):
        matrix[i] = input().split()

    end = 0
    for i in range(100):
        if matrix[99][i] == '2':
            end = i
            break

    now_x , now_y = end, 99
    way = 0  # up:0 , left:-1, right:1
    while now_y != 0:
        if now_x != 0 and way != 1 and matrix[now_y][now_x - 1] == '1':
            way = -1
            now_x -= 1
        elif now_x != 99 and way != -1 and matrix[now_y][now_x + 1] == '1':
            way = 1
            now_x += 1
        else:
            way = 0
            now_y -= 1

    print(f"#{testcase} {now_x}")