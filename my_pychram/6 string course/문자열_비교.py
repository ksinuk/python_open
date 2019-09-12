import sys
sys.stdin = open("문자열_비교_input.txt", "r")

def myfind(p, t,test):
    ti = 0
    while ti <= len(t) - len(p):
        for pi in range(len(p) - 1, -1, -1):
            if t[ti + pi] != p[pi]:
                for i in range(pi, -1, -1):
                    if t[ti + pi] == p[i]:
                        ti = ti +pi-i
                        break
                else:
                    ti += pi + 1
                break
            elif pi == 0:
                return 1
    return 0

#---------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    p = input()
    x = input()

    out = myfind(p, x, test_case)

    print(f"#{test_case} {out}")
