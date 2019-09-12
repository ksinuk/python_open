import sys
sys.stdin = open("cemical_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size = int(input()) # 창고의 가로,세로의 길이
    table = [[] for i in range(size)] # 창고의 상황
    warning = [] # 위험물 목록
    for i in range(size): # 창고 상황 입력
        table[i] = list(map(int , input().split()))
    # 입력 완료 -----------------------------------------------
    for y in range(size):
        for x in range(size):
            if table[y][x]: # 위험물 발견
                dy , dx = 0,0
                for yy in range(y,size): # 위험물의 세로길이 측정
                    if  table[yy][x]==0:
                        dy = yy-y
                        break
                for xx in range(x,size): # 위험물의 가로길이 측정
                    if  table[y][xx]==0:
                        dx = xx-x
                        break

                warning.append([dy,dx])  # 위험물의 정보 입력
            
                for yy in range(y,y+dy): # 위험물 제거
                    for xx in range(x,x+dx):
                        table[yy][xx] = 0
    # 탐색 완료 ,  정렬 시작 ------------------------------------------------
    len_warning = len(warning) # 위험물의 양
    for i in range(1,len_warning): # 삽입 정렬
        for j in range(i,0,-1): 
            j_area = warning[j][0]*warning[j][1]
            jm1_area = warning[j-1][0]*warning[j-1][1]
            if j_area < jm1_area or ( j_area == jm1_area and warning[j][0] < warning[j-1][0] ):
                warning[j-1] , warning[j] = warning[j] , warning[j-1]
            else:
                break

    out = [str(len_warning)]
    for i in range(len_warning):
        out.append(str(warning[i][0]))
        out.append(str(warning[i][1]))
    out = ' '.join(out)

    print(f"#{test_case} {out}")