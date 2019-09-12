def select_sort(a,reverse=0):
    for i in range(0,len(a)-1):
        min=i
        for j in range(i+1,len(a)):
            if reverse==0 and a[min] > a[j] or reverse and a[min] < a[j]:
                min=j
        a[i],a[min] = a[min],a[i]

data = [4,4,25,10,22,11]
select_sort(data)
print(data)
select_sort(data,1)
print(data)