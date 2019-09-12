import sys
sys.stdin = open("elec_bus_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    bus_range , road_range , station_cnt = map(int, input().split())
    list_station = list(map(int, input().split()))
    
    out = 0 # 출력값
    point = 0 # 현재 위치
    prev = 0 # 이전 위치
    while 1:
        if out<0:break # 도착점 까지 이동 불가
        prev = point
        point += bus_range #이전 및 현재 위치 계산
        if point >= road_range:break # 도착점 도달
        else:
            while 1:
                temp=0
                for ii in range(station_cnt): # if point in list_station: 계산 과정
                    if list_station[ii] == point:
                        temp=1
                        break
                if temp: # if point in list_station: 확인 과정
                    out+=1
                    break
                else: # 가장 가까운 주유소 다시 찾기
                    point-=1
                    if prev == point: # 주유소를 찾을 수 없다
                        out=-1
                        break
    if out>0:print(f"#{test_case} {out}")
    else : print(f"#{test_case} 0")
            