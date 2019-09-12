def sort(data):
    for i in range(len(data)-1):
        min=i
        for j in range(i,len(data)):
            if data[min]>data[j]:
                min=j
        data[i] , data[min] = data[min] , data[i]


indata = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
outdata = [[0]*5 for i in range(len(indata))]


data = []
for i in indata:
    data+=i
sort(data)

x,y = 0,0
range_x_orign=len(indata)-1
range_x=range_x_orign
x2 = 0 #0:right 1:left
range_y_orign=len(indata)-2
range_y=range_y_orign
y2 = 0 #down 1:up
xy = 0 #0:x 1:y
data_i=0

ssize = len(indata)*len(indata)
while data_i != ssize:
    inx = data[data_i]
    data_i += 1

    outdata[y][x] = inx

    if xy==0:
        if range_x>0:
            range_x-=1
            x = x - 1 if x2 else x + 1
        else:
            xy=1
            range_x_orign-=1
            range_x = range_x_orign
            x2 = (x2 + 1) % 2

            y = y - 1 if y2 else y + 1
    else :
        if range_y > 0:
            range_y -= 1
            y = y - 1 if y2 else y + 1
        else:
            xy=0
            range_y_orign -= 1
            range_y = range_y_orign
            y2 = (y2 + 1) % 2

            x = x - 1 if x2 else x + 1

for i in outdata:
    for j in range(len(i)):
        if j<len(i)-1:
            print(f"{i[j]:2}",end=' ')
        else:
            print(f"{i[j]:2}")

















