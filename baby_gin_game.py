num =input()
if len(num)!=6:
    print("error")
    exit()

c = [0]*12

for i in range(6):
    c[int(num[i])]+=1

i = tri = rum = 0
while i<10:
    if c[i]>=3:
        c[i]-=3
        tri+=1
        continue
    if c[i] >=1 and c[i+1]>=1 and c[i+2]>=1:
        c[i]-=1
        c[i+1] -= 1
        c[i+2] -= 1
        rum+=1
        continue
    i+=1

if tri+rum==2:print("bab=gin")
else:print("not")




