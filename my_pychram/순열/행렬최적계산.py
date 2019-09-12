def perfact(data,sums):
    size = len(data)
    if size<3:
        return sums
    
    mins = -1
    for i in range(1,size-1):
        new = data[0:i]+data[i+1:size]
        temp = data[i-1]*data[i]*data[i+1]
        out = perfact(new,sums+temp)
        if mins==-1:
            mins = out
        else:
            if mins > out:
                mins = out

    return mins


def cal(datain):
    size = len(datain)
    table = [[0 for i in range(size+1)] for j in range(size+1)]
    out = 0

    for x in 

    return out





data = [3,4,5,6,8,3,6,8,11]
minout = perfact(data,0)
out = cal(data)
print(minout,out)