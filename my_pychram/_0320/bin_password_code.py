import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('print.txt','w')
#---------------------------------
def cal(patterns):
    ysize , xsize = map(int , input().split())
    maps = ''
    code = [0 for i in range(8)]

    for y in range(ysize):
        strx = input()
        if maps!='':continue

        for x in range(xsize-1,-1,-1):
            if strx[x]=='1' and x-55>=0:
                maps = strx[x-55:x+1]
                break

    for i in range(8):
        password = maps[i*7:i*7+7]
        for j in range(10):
            if patterns[j]==password:
                code[i] = j
                break

    out = 0
    for i in range(8):
        if i%2==0:
            out+=3*code[i]
        else:
            out+=code[i]


    return sum(code) if out%10==0 else 0

#--------------------------------
patterns = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

Ntest = int(input())
for testcase in range(1,Ntest+1):
    out = cal(patterns)
    print("#{} {}".format(testcase,out))