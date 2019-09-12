def marge_sort(data):
    if len(data)<=1:
        return data
    elif len(data)==2:
        if data[0]>data[1]:
            return [data[1],data[0]]
        return [data[0],data[1]]
    
    mid = len(data)//2
    left = data[:mid]
    right = data[mid:]
    left = marge_sort(left)
    right = marge_sort(right)

    result = []
    while len(left)>0 and len(right)>0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    while len(left):
        result.append(left.pop(0))
    while len(right):
        result.append(right.pop(0))

    return result

def marge_sort_dp(data):
    if len(data)<=1:
        return data

    result = data[:]
    step , index = 1,0
    while step<len(result):
        now = index
        if index+step>=len(result):
            step+=step
            index=0
            continue
        left = result[index:index+step]
        index+=step
        right = []
        if index+step>=len(result):
            right = result[index:len(result)]
        else:
            right = result[index:index+step]
        index+=step

        while len(left)>0 and len(right)>0:
            if left[0] < right[0]:
                result[now]=left.pop(0)
            else:
                result[now]=right.pop(0)
            now+=1
    
        while len(left):
            result[now]=left.pop(0)
            now+=1
        while len(right):
            result[now]=right.pop(0)
            now+=1

    return result

a = [69,10,30,2,16,8,31,23,1,1]
b = a[:]
print(a)
c = marge_sort(a)
d = marge_sort_dp(b)
print(c)
print(d)