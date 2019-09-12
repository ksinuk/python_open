import sys
sys.stdin = open("글자수_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    inx = list(input())
    inx = list(set(inx))
    table = input()

    out = 0
    for c in inx:
        temp=0
        for text in table:
            if text==c:
                temp+=1
        if temp>out:
            out = temp

    print(f"#{test_case} {out}")


