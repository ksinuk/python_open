import sys
sys.stdin = open("정식이의_은행업무_input.txt", "r")
sys.stdout = open("정식이의_은행업무_output.txt", "w")

def make_num(arr,n):
    out = 0
    size = len(arr)
    for i in range(size):
        out += arr[size-1-i]*(n**i)
    return out

def if2_1(n):
    n = -n if n<0 else n
    two , out = 1 , 0
    while two<=n:
        if two==n:
            return out        
        two , out= 2*two , out+1
    return -1

T = int(input())
for test_case in range(1, T + 1):
    out = -1
    in2 = list(map(int,list(input())))
    x2 = make_num(in2,2)
    in3 = list(map(int,list(input())))
    x3 = make_num(in3,3)
    d = x2-x3

    for i2 in range(len(in2)):
        in2[i2] = (in2[i2]+1)%2
        y2 = x2-(2**(len(in2)-1-i2)) if in2[i2]==0 else x2+(2**(len(in2)-1-i2))
        ok = 0
        for i3 in range(len(in3)):
            in3[i3] = (in3[i3]+1)%3
            y3 = x3-2*(3**(len(in3)-1-i3)) if in3[i3]==0 else x3+(3**(len(in3)-1-i3))
            if y3==y2:
                out , ok = y2 , 1
                break
            in3[i3] = (in3[i3]+1)%3
            y3 = y3-2*(3**(len(in3)-1-i3)) if in3[i3]==0 else y3+(3**(len(in3)-1-i3))
            if y3==y2:
                out , ok = y2 , 1
                break
            in3[i3] = (in3[i3]+1)%3
        in2[i2] = (in2[i2]+1)%2
        if ok:
            break

    print("#{} {}".format(test_case,out))