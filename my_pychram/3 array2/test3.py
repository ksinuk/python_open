


data = [1,2,3]
for i in range(1<<len(data)):
    print(f"bit {i:2} : ",end='')
    for j in range(len(data)):
        out = (i&1<<(len(data)-1-j))>>(len(data)-1-j)
        print(out,end='')
    print(" , data : ",end='')
    for j in range(len(data)):
        out = (i&1<<(len(data)-1-j))>>(len(data)-1-j)
        if out:
            print(data[j],end=',')


    print()
