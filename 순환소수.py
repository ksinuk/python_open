N=int(input())
for index in range(1,N+1):
    a ,b = map(int , input().split())
    out = str(a//b)
    a=a%b
    if a>0:
        out+='.'
    
    list_num = []
    len_prev = len(out)
    cut = -1
    while a>0:
        a*=10
        temp = str(a//b)
        out += temp
        a=a%b
        temp += str(a)
        if a==0:
            cut=-1
            break
        elif temp in list_num:
            cut = list_num.index(temp)+len_prev
            break
        else:
            list_num.append(temp)
    if cut>=0:
        out = out[0:cut]+'('+out[cut:-1]+')'
    print(f"#{index} {out}")