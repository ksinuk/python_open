import sys
sys.stdin = open("사칙연산_input.txt","r")

def cal(table,num):
    if len(table[num])==1:
        return table[num][0]
    a = cal(table,table[num][1])
    b = cal(table,table[num][2])

    c = table[num][0]
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='/':
        return a/b
    elif c=='*':
        return a*b

for __ in range(1,11):
    size = int(input())
    table = [0]*(size+1)
    for i in range(1,size+1):
        li = list(input().split())
        li[0] = int(li[0])
        if len(li)==4:
            li[2] = int(li[2])
            li[3] = int(li[3])
            table[li[0]] = [li[1] , li[2] ,li[3]]
        else:
            li[1] = float(li[1])
            table[li[0]] = [li[1]]

    out = cal(table,1)
    print("#{} {}".format(__,int(out)))






