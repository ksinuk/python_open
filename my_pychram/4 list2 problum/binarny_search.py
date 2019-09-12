import sys
sys.stdin = open("sample_input_binary_search.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    page, a, b = map(int, input().split())
    b_low = a_low = 1
    b_high = a_high = page

    out=''
    while 1:
        a_mid = (a_low+a_high)//2
        b_mid = (b_low+b_high)//2

        if a_mid==a and  b_mid ==b:
            out='0'
            break
        elif a_mid==a:
            out='A'
            break
        elif b_mid==b:
            out='B'
            break

        if a_mid<a:
            a_low = a_mid
        else:
            a_high = a_mid

        if b_mid<b:
            b_low = b_mid
        else:
            b_high = b_mid



    print(f"#{test_case} {out}")
