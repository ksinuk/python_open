import sys
sys.stdin = open("Magnetic_input.txt", "r")

for testcase in range(1,11):
    out = 0
    input()
    table = [[0 for i in range(100)] for i in range(100)] # 1:N , 2:S
    for i in range(100):
        table[i] = list(map(int,input().split()))
    #---------------- 입력 완료 -------------------------------

    for x in range(100):
        n=0
        for y in range(100):
            now = table[y][x]
            if now==1:n=1
            elif now==2:
                out+=n
                n=0

    print(f'#{testcase} {out}')