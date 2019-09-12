n= 5
out = 0
array = [0 for i in range(100)]
index = -1

while 1:
    if n==1 and out==0:
        out=1
    elif out:
        if index==0:
            break
        else:
            array[index-1]*=array[index]
            index-=1
    else:
        index+=1
        array[index]=n
        n-=1
    print(array[0:index+1],index,out)

print(array[0])

