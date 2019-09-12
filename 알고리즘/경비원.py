import sys
sys.stdin = open("경비원.txt","r")

for __ in range(2):
    size_x , size_y = map(int,input().split())
    num = int(input())
    stores = [[0,0] for i in range(num)] #  1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽
    for i in range(num):
        stores[i][0] , stores[i][1] = map(int,input().split())
    man=[0,0]
    man[0] , man[1] = map(int,input().split())
    # 입력완료 ----------------------
    out = 0
    if man[0]==1:
        for i in range(num):
            if stores[i][0]==1:
                out += abs(man[1]-stores[i][1])
            elif stores[i][0]==2:
                out += size_y
                temp1 = man[1] + stores[i][1]
                temp2 = 2*size_x - man[1] - stores[i][1]
                out += temp1 if temp1<temp2 else temp2
            elif stores[i][0]==3:
                out += man[1] + stores[i][1]
            elif stores[i][0]==4:
                out += size_x - man[1] + stores[i][1]
    elif man[0]==2:
        for i in range(num):
            if stores[i][0]==1:
                out += size_y
                temp1 = man[1] + stores[i][1]
                temp2 = 2*size_x - man[1] - stores[i][1]
                out += temp1 if temp1<temp2 else temp2
            elif stores[i][0]==2:
                out += abs(man[1]-stores[i][1])
            elif stores[i][0]==3:
                out += man[1] + size_y - stores[i][1]
            elif stores[i][0]==4:
                out += size_x - man[1] + size_y - stores[i][1]
    elif man[0]==3:
        for i in range(num):
            if stores[i][0]==1:
                out += man[1] + stores[i][1]
            elif stores[i][0]==2:
                out += size_y - man[1] + stores[i][1]
            elif stores[i][0]==3:
                out += abs(man[1]-stores[i][1])
            elif stores[i][0]==4:
                out += size_x
                temp1 = 2*size_y - man[1] - stores[i][1]
                temp2 = man[1] + stores[i][1]
                out += temp1 if temp1<temp2 else temp2
    elif man[0]==4:
        for i in range(num):
            if stores[i][0]==1:
                out += man[1] + size_x - stores[i][1]
            elif stores[i][0]==2:
                out += size_y - man[1] + size_x - stores[i][1]
            elif stores[i][0]==3:
                out += size_x
                temp1 = 2*size_y - man[1] - stores[i][1]
                temp2 = man[1] + stores[i][1]
                out += temp1 if temp1<temp2 else temp2
            elif stores[i][0]==4:
                out += abs(man[1]-stores[i][1])

    print(out)
    