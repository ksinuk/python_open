import sys
sys.stdin = open("이진수2_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    x = float(input())

    out = ''
    for c in range(12):
        x*=2
        if x>=1:
            out+='1'
            x-=1
        else:
            out+='0'
        if x==0:
            break

    if x>0:    
        print("${} overflow".format(test_case))
    else:
        print("${} {}".format(test_case,out))