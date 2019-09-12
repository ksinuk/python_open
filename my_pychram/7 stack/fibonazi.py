fibo_list = [0,1]
def fibonazi(n,func=2,deep=1):
    global fibo_list

    if n<=len(fibo_list)-1:
        return fibo_list[n]

    if func==0: # 제귀
        return fibonazi(n-1) + fibonazi(n-2)
    elif func==1: # 제귀 + memoize
        out = fibonazi(n-1,1,deep+1) + fibonazi(n-2,1,deep+1)
        if n == len(fibo_list):
            fibo_list.append(out)
        return out
    elif func==2: # 비제귀 + memoize
        for i in range(len(fibo_list),n+1):
            fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
        return fibo_list[n]

    stack_func = [n]
    out = 0
    while 1:
        m = stack_func.pop()
        if m < len(fibo_list) - 1:
            out = fibo_list[m]
        elif m == len(fibo_list):
            fibo_list.append(fibo_list[m-1]+fibo_list[m-2])
            out = fibo_list[m]
        else:
            stack_func.append(m)
            stack_func.append(m-1)
            stack_func.append(m-2)

        if len(stack_func)==0:
            return out


#---------------------------

# for i in range(1000,49,-1):
#     print(f"{i} : {fibonazi(i)} , {fibonazi(i)}")
print(f"{10} : {fibonazi(10,3)}")