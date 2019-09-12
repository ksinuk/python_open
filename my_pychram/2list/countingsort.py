def counting_sort(data):
    max = data[0]
    min = max
    for i in data:
        if max<i:
            max = i
        if min>i:
            min = i

    cnt_list = [0 for ii in range(max-min+1)]
    for i in data:
        cnt_list[i-min]+=1
    i=0
    while i<max-min:
        cnt_list[i+1]+=cnt_list[i]
        i+=1
    out = [0 for ii in range(len(data))]
    for i in range(len(data)-1,-1,-1):
        temp = data[i]-min
        point = cnt_list[temp]
        cnt_list[temp]-=1
        out[point-1] = data[i]

    return out


data = [9,9,7,6,6,9,3,2,6,21]
out = counting_sort(data)
print(out)