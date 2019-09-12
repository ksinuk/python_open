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
n = int(innum/6)

num = []
for i in range(0,n+1):
    a1 = 6*i+1
    a2 = 6*i+5

    num.append(a1)
    num.append(a2)
if num[len(num)-1] > innum:
    num.pop()
    if num[len(num)-1] > innum:
        num.pop()



sosus=[2,3,5]


for x in num:
    a1 = 6*i+1
    a2 = 6*i+5
    if itis_sosu(a1,sosus) and not(a1 in sosus):
        sosus.append(a1)
    if itis_sosu(a2,sosus) and not(a2 in sosus):
        sosus.append(a2)

with open("sosu.txt","w") as f:
    sosus.sort()
    prev = 0

    for now in sosus:
        y = now - prev
        f.write(f"{now} : {y}\n")
        prev = now
