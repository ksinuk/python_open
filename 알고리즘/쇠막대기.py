import sys
sys.stdin = open("쇠막대기.txt", "r")

for __ in range(1):
    inline = list(input())
    table = []
    for c in inline:
        if c==')' and table[-1]=='(':
            table[-1]='L'
        else:
            table.append(c)
    
    out = 0
    stack = [0 for i in range(len(table)+1)]
    index = 0
    for c in table:
        if c=='(':
            index+=1
        elif c=='L':
            stack[index]+=1
        elif c==')':
            stack[index-1] += stack[index]
            out += stack[index]+1
            stack[index] = 0
            index-=1
    
    print(out)



