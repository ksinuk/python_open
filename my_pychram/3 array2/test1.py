arr = [[0,1,2,3],[4,5,6,7],[8,9,10,11]]
leny=3
lenx=4

for i in range(leny):
    for j in range(lenx):
        print(arr[i][j],end=" ")
    print()
print('------------')
for x in range(lenx):
    for y in range(leny):
        print(arr[y][x], end=" ")
    print()
print('------------')

for y in range(leny):
    for x in range(lenx):
        print(arr[y][x+(lenx-1-2*x)*(y%2)],end=' ')
    print()