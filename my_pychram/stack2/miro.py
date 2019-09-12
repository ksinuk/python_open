import sys
sys.stdin = open("miro_input.txt", "r")

class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

def select_direct(maps, arrow, now, size):
    if now.x < size - 1 and maps[now.y][now.x + 1] !='1' and arrow != 4: return 6
    elif now.y < size - 1 and maps[now.y + 1][now.x] !='1' and arrow != 2: return 8
    elif now.x > 0 and maps[now.y][now.x - 1] !='1' and arrow != 6: return 4
    elif now.y > 0 and maps[now.y - 1][now.x] !='1' and arrow != 8: return 2
    else:
        return 0

def cal_only(maps, now, size):
    temp = 0
    if now.x < size - 1 and maps[now.y][now.x + 1] !='1': temp += 1
    if now.y < size - 1 and maps[now.y + 1][now.x] !='1': temp += 1
    if now.x > 0 and maps[now.y][now.x - 1] !='1': temp += 1
    if now.y > 0 and maps[now.y - 1][now.x] !='1': temp += 1
    return temp

def next_point(now, arrow):
    if arrow == 6:
        now.x += 1
    elif arrow == 8:
        now.y += 1
    elif arrow == 4:
        now.x -= 1
    elif arrow == 2:
        now.y -= 1
    return now

T = int(input())
for test_case in range(1, T + 1):
    SIZE = int(input())

    out = 2
    maps = [[] for i in range(SIZE)]
    for y in range(SIZE):
        maps[y] = list(input())

    now = Point(-1, -1)
    for x in range(SIZE):
        breakx = 0
        for y in range(SIZE):
            if maps[y][x] =='2':
                now.y = y
                now.x = x
                breakx = 1
                break
        if breakx: break
    if now.x < 0: out = 0
    # ------------- 입력완료 --------------------------

    history = [0 for i in range(SIZE * SIZE)]
    history_size = 0
    arrow = 0  # keypad : e=6 , n=8 , w=4 , s=2 , stop=0

    while out == 2:
        if maps[now.y][now.x] =='3':  # 도착
            out = 1
            break
        maps[now.y][now.x] = '1'

        temp = cal_only(maps, now, SIZE)  # 방향 결정 파트
        if temp == 0:
            if history_size == 0:
                out = 0
                break
            now = history[history_size - 1]
            history_size -= 1
            arrow = 0
            continue
        elif temp != 1:
            temp_point = Point(x=now.x, y=now.y)
            history[history_size] = temp_point
            history_size += 1
        arrow = select_direct(maps, arrow, now, SIZE)

        now = next_point(now, arrow)

    print(f"#{test_case} {out}")




