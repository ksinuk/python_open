import sys
sys.stdin = open("sample_input_color_play.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    table = [[[0, 0] for i in range(10)] for i in range(10)]
    num = int(input())
    for i in range(num):
        x1,y1,x2,y2,color = map(int, input().split())
        color-=1

        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                table[y][x][color]=1

    out=0
    for x in range(10):
        for y in range(10):
            if table[y][x][0] and table[y][x][1]:
                out+=1

    print(f"#{test_case} {out}")


