a,b = map(int,input().split())
if a>b:
    a,b=b,a
if a==1:
    a=2

cut = int(b**0.5)
sosu = [0]*cut
sosu[0] = 2;sosu[1] = 3;sosu[2] = 5
sosu_size = 3

num = 7
while num<=cut:
    temp = int(num**0.5)
    issosu = 1
    for i in range(sosu_size):
        if temp < sosu[i]:break
        if num%sosu[i]==0:
            issosu = 0
            break
    if issosu:
        sosu[sosu_size] = num;sosu_size+=1
    if num%6==1:
        num+=4
    else:
        num+=2

out_sosu = []
out_size = 0
if b>a:
    out_sosu = [0]*(b-a)
if a==2:
    a=5
    out_sosu[0] = 2
    out_size = 1
    if b>2:
        out_sosu[1] = 3
        out_size += 1
elif a==3:
    a=5
    out_sosu[0] = 3
    out_size = 1
elif a%6==0:
    a+=1
elif 1<a%6<5:
    a += 5-a%6

for num in range(a,b+1):
    cut = int(num**0.5)
    ok = 1
    for i in range(sosu_size):
        if sosu[i]>cut:break
        if num%sosu[i]==0:
            ok=0
            break
    if ok:
        out_sosu[out_size] = num
        out_size+=1
    if num%6==1:
        num+=4
    else:
        num+=2

print(out_size)
print(out_sosu[0]+out_sosu[out_size-1])


    

    

