def fact(x):
    y=1
    i=1
    while i<=x:
        y*=i
        i+=1
    return y


inx = input("input : ")
inx = int(inx)
print("input : {}".format(inx))
if inx <2:
    print("exit")
    exit()

lists = []
out = []



now = inx

while 1:
    cut = int(now**0.5)
    i=2
    while i<=cut:
        if now%i==0:
            lists.append(int(i))
            now = now/i
            cut=int(now**0.5)
            i=2
        else :
            i+=1
    out.append(int(now))
    if lists:
        now = lists.pop()
    else :
        break

out.sort()
print(out)
