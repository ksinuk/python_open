def bubblesort(data):
    for index in range(len(data)-1,0,-1):
        for i in range(index):
            if data[i] > data[i+1]:
                temp = data[i+1]
                data[i+1] = data[i]
                data[i] = temp




data = [9,8,7,6,5,4,3,2,1]
bubblesort(data)
print(data)