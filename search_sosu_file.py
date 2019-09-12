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

f = open("sosu_file.txt","w")
f.write("2 : 2\n")
f.write("3 : 1\n")
f.write("5 : 2\n")

prev=5
for index,x in enumerate(num):
    f.write(f"{x} : {x-prev}\n")
    prev = x

    i=index+1
    len_num = len(num)
    while i<len_num:
        if num[i]%x==0 :
            num.remove(num[i])
            len_num -=1
        else :
            i+=1
    
f.close()