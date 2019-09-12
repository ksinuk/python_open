def itis_sosu(x,sosus):
    if (x<2):
        return False

    sqrt_x=int(x**0.5)
    if (sqrt_x<2):
        return True

    cut = search_list(sosus,sqrt_x)

    for i in range(0,cut):
        if x%sosus[i]==0:
            return False
    return True


def search_list(sosus,x):
    low = 0
    high = len(sosus)-1
    now = len(sosus)//2

    while high-low<2:
        if sosus[now]==x:
            return now
        elif sosus[now]>x:
            high = now
            now = int((low+now-1)/2)
        elif sosus[now]<x:
            low = now
            now = int((now+1+high)/2)

    return now

innum = int(input('n : '))
if (innum<2):
    print("제대로 적어라")
n = innum//6

num = []
for i in range(1,n+1):
    a1 = 6*i+1
    a2 = 6*i+5

    if a1%2 and a1%3 and a1%5:
        num.append(a1)
    if a2%2 and a2%3 and a2%5:
        num.append(a2)

if num[len(num)-1] > innum:
    num.pop()
    if num[len(num)-1] > innum:
        num.pop()

sosus=[2,3,5]

index = 0
for x in num:
    ''' if itis_sosu(x,sosus) and not(x in sosus):
        sosus.append(x)
    '''

    ''' if x==0:
            continue
        if itis_sosu(x,sosus) and not(x in sosus):
            sosus.append(x)
        
        i=0
        len_num = len(num)
        while i<len_num:
            if num[i] > x:
                if num[i]%x==0 :
                    num[i]=0
            i+=1
    '''
    sosus.append(x)

    i=index+1
    len_num = len(num)
    while i<len_num:
        if num[i]%x==0 :
            num.remove(num[i])
            len_num -=1
        else :
            i+=1

    index+=1 

    # for i in num:
    #     if i>x:
    #         if i%x==0:
    #             num.remove(i)
    

with open("sosu.txt","w") as f:
    sosus.sort()
    prev = 0

    for now in sosus:
        y = now - prev
        f.write(f"{now} : {y}\n")
        prev = now
