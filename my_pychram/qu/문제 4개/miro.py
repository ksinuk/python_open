import sys
sys.stdin = open("miro_input.txt", "r")

class Point: # 좌표
    def __init__(self, y=-1, x=-1):
        self.y = y
        self.x = x

class Terminal: # 큐 형식의 교차로 목록
    def __init__(self,size):
        self.start = 0
        self.end = -1
        self.terminal = [[0,0] for i in range(size * size*2)]
    
    def input(self,point,distance): # 입력 
        for now in self.terminal[self.start:self.end+1]:
            if point==now[0]:
                now[1] = distance if distance<now[1] else now[1]
                return 0
        self.end +=1
        self.terminal[self.end] = [point,distance]
        return 0

    def output(self): # 출력
        self.start +=1
        return self.terminal[self.start-1]

def select_direct(maps, arrow, now, size): # 가야 할 방향 정하기
    if now.x < size - 1 and maps[now.y][now.x + 1] !='1' and arrow != 4: return 6
    elif now.y < size - 1 and maps[now.y + 1][now.x] !='1' and arrow != 2: return 8
    elif now.x > 0 and maps[now.y][now.x - 1] !='1' and arrow != 6: return 4
    elif now.y > 0 and maps[now.y - 1][now.x] !='1' and arrow != 8: return 2
    else: return 0

def cal_only(maps, now, size): # 갈 수 있는 방향의 갯수 구하기
    temp = 0
    if now.x < size - 1 and maps[now.y][now.x + 1] !='1': temp += 1
    if now.y < size - 1 and maps[now.y + 1][now.x] !='1': temp += 1
    if now.x > 0 and maps[now.y][now.x - 1] !='1': temp += 1
    if now.y > 0 and maps[now.y - 1][now.x] !='1': temp += 1
    return temp

def next_point_cal(now, arrow): # 다음 좌표 이동
    if arrow == 6: now.x += 1
    elif arrow == 8: now.y += 1
    elif arrow == 4: now.x -= 1
    elif arrow == 2: now.y -= 1
    return now

def find_point(thisis,maps): # 시작점 찾기
    out = Point(-1, -1)
    for x in range(size):
        for y in range(size):
            if maps[y][x] ==thisis:
                out.y = y; out.x = x
                return out

#-------------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    size = int(input())

    out = -2
    maps = [[] for i in range(size)] # 미로 지도
    for y in range(size):
        maps[y] = list(input())

    start = find_point('2',maps) # 시작점 계산
    if start.x < 0: out = 0
    # ------------- 입력완료 --------------------------

    terminal = Terminal(size) # 교차로 목록
    terminal.input(start , 0) # 시작점 입력

    arrow = 0  # keypad : e=6 , n=8 , w=4 , s=2 , stop=0

    while out<0 and terminal.start<=terminal.end:
        now_terminal = terminal.output()
        now = now_terminal[0]
        dist_orign = now_terminal[1]

        if maps[now.y][now.x] == '3': # 가장빠른 도착지의 경로 발견
            out = dist_orign
            break
        maps[now.y][now.x] = '1' # 지나간 길은 매꾼다.

        # 각 교차점에서 다음 교차점 찾기
        for i in range(4):
            arrow = select_direct(maps, 0, now, size) # 지나가야 할 방향 계산
            if arrow==0: # 막다른 길이다.
                break

            next_point = Point(y=now.y , x=now.x) # 지나 가는 길의 좌표
            distance = dist_orign # 그 동안의 거리
            while 1:
                next_point = next_point_cal(next_point, arrow) # 다음 좌표로 이동
                distance+=1
                if maps[next_point.y][next_point.x]=='3': # 도착점 발견 (가장 빠른 길은 아님)
                    terminal.input(next_point,distance) # 도착점 이동
                    break

                arrow_temp = cal_only(maps, next_point, size) # 교차로 인지 확인
                if arrow_temp==0: break # 막다른 길
                elif arrow_temp!=1: # 교차점 발견
                    if dist_orign+1==distance:
                        maps[next_point.y][next_point.x] = '1'
                    terminal.input(next_point,distance)
                    break
                else: # 교차점이 아님
                    maps[next_point.y][next_point.x] = '1'
                    arrow = select_direct(maps, arrow, next_point, size)
            if out>=0:break

        if out>=0 or terminal.start>terminal.end:break

        min_dist , min_i = size * size , -1 # 미탐색 노드 중에서 시작점과 가장 가까운 노드 찾기
        for i in range(terminal.start , terminal.end+1):
            if terminal.terminal[i][1] < min_dist:
                min_i , min_dist = i , terminal.terminal[i][1]
        terminal.terminal[min_i] , terminal.terminal[terminal.start] = terminal.terminal[terminal.start] ,terminal.terminal[min_i]

    out = 0 if out<1 else out-1
    print(f"#{test_case} {out}")




