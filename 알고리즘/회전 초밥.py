import sys
sys.stdin = open("회전_초밥_input.txt","r")

N = int(input())
for __ in range(N):
    size , susi_num , max_eat , cupon = map(int , input().split())
    max_out = 1
    out = 1
    history = [0]*(susi_num+1)
    history[cupon] = 1
    nows = [0]*max_eat
    index = 0
    in_history = [0]*(max_eat+2)

    for ini in range(size+max_eat+2):
        if nows[index]!=0:
            history[nows[index]]-=1
            if history[nows[index]]==0:
                out-=1

        temp = 0
        if ini < size:
            temp = int(input())
            if ini < max_eat+2:
                in_history[ini] = temp
        else:
            temp = in_history[ini-size]
        nows[index] = temp
        index = (index+1)%max_eat

        history[temp] +=1
        if history[temp]==1:
            out+=1
            if max_out < out:
                max_out = out

    print(max_out)
