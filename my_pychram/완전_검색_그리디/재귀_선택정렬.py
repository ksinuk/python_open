def select_sort(arr):
    size = len(arr)
    if size==1:return arr
    
    mini = 0
    for i in range(1,size):
        if arr[mini]>arr[i]:
            mini = i  

    arr[mini] , arr[0] = arr[0] , arr[mini]
    b = select_sort(arr[1:size])
    for i in range(len(b)):
        arr[i+1] = b[i]

    return arr


arr = [9,7,6,5,4,3,2,4,5,6,7,1]
print(arr)
arr = select_sort(arr)
print(arr)

