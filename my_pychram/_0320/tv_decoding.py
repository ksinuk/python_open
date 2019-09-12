import sys
sys.stdin = open('tv_input.txt','r')
sys.stdout = open('print.txt','w')
#-------------------------------------
patterns = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']
table16 = ['0000' ,'0001' ,'0010' ,'0011' ,'0100' ,'0101' ,'0110' ,'0111' , '1000' ,'1001' ,'1010' ,'1011' ,'1100' ,'1101' ,'1110' ,'1111']

def change(c):
    c = ord(c)
    if c>=ord('A'):
        return c-ord('A')+10
    else:
        return c-ord('0')

def search(inmap , ysize , xsize , iny,inx):
    temp_str , out = '' , ''
    cnt , pre = 0 , '0'
    for x in range(inx , xsize):
        temp_str = table16[change(inmap[iny][x])]
        out+=temp_str

        for j in range(4):
            if temp_str[j] != pre:
                pre = temp_str[j]
                cnt+=1
        
        if cnt>31:
            break

    return out

def decoding(password):
    global patterns,table16

    password = password.strip('0')

    add0 = (56-len(password)%56)%56
    password = '0'*add0 + password
    len_pass = len(password)
    minlen = len_pass//56
    code = [0 for i in range(8)]

    for index in range(8):
        pattern = 0
        k = len_pass-1-minlen*index*7
        for i in range(7):
            if password[k-minlen*i]=='1':
                pattern += (1<<i)

        for i in range(10):
            if patterns[i] == pattern:
                code[7-index] = i
                break
    #-----------------------------
    out = 0
    for i in range(8):
        if i%2==0:
            out+=3*code[i]
        else:
            out+=code[i]
    return sum(code) if out%10==0 else 0


def cal():
    ysize , xsize = map(int , input().split())

    pre ,  temp = '' , ''
    inmap = []
    for y in range(ysize):
        temp = input()
        if pre!=temp:
            pre = temp
            inmap.append(temp)
    ysize = len(inmap)
    del pre
    del temp

    out = 0
    for y in range(ysize):
        x=0
        while x<xsize:
            if inmap[y][x]!='0' and (y==0 or inmap[y-1][x]=='0'):
                maps = search(inmap , ysize , xsize , y,x)
                x += len(maps)//4
                out += decoding(maps)
            else:
                x+=1
    
    return out

#----------------------------------------
for i in range(10):
    num = 0
    pattern = patterns[i]
    for j in range(7):
        num += num + int(pattern[j])
    patterns[i] = num


Ntest = int(input())
for testcase in range(1,Ntest+1):
    out = cal()
    print("#{} {}".format(testcase,out))