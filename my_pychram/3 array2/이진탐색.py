def binarny_search(a,key):
    start = 0
    end = len(a)-1
    if a[0]>key:
        return ['pre','start']
    elif a[end]<key:
        return ['after', 'end']


    while start<=end:
        mid = (start + end)//2
        if key == a[mid]:
            return [mid,mid]
        elif key < a[mid]:
            end = mid
        else:
            start = mid

        if start+1==end:
            return [start,end]
    return ['error','error']


key = 18
data = [2,4,7,9,11,19,23]
print(binarny_search(data,key))