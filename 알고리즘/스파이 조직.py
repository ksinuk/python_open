import sys
sys.stdin = open("spy_input.txt","r")

for __ in range(1):
    step , password = input().split()
    step = int(step)

    num = ''
    now = 0
    out = []
    for c in password:
        if c!='<' and c!='>':
            num += c
        else:
            if now==step and num:
                out.append(int(num))
                num = ''
            else:
                num = ''

            if c=='<':
                now +=1
            elif c=='>':
                now-=1
    
    for i in range(len(out)-1):
        print(out[i],end=' ')
    print(out[-1])


