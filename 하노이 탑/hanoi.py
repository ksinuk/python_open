# 아래에 코드를 작성해주세요.
count=0
deep_max = -1
deep_min = 0
cnt_list = []
deep_list = []
start_list = [0,0,0]
end_list = [0,0,0]

# ------------------------------------------------
def move_pan(list_x,start,end,deep,f):
    global count , deep_max , deep_min , start_list , end_list , deep_list , cnt_list
    outstr=['a','b','c']

    temp = list_x[start].pop()
    list_x[end].append(temp)
    f.write(f'{list_x[0]}, {list_x[1]}, {list_x[2]}, {outstr[start]} -> {outstr[end]} , deep : {deep}\n')

    count+=1
    cnt_list[temp-1]+=1
    start_list[start]+=1
    end_list[end]+=1

    return list_x
# ------------------------------------------------
def hanoi(list_x,num,start,end,f,deep=1):
    if start == end :
        print('start == end error')
        return 'error'
    if len(list_x[start])<num:
        print('len(list_x[start])<num error')
        return 'error'
    
    global count , deep_max , deep_min , start_list , end_list , deep_list , cnt_list
    
    if deep_max < deep:
        deep_max = deep 
    if deep_min > deep:
        deep_min = deep
    deep_list[deep] +=1
    
    mid = 3-start-end    
    
    if num==1:
        list_x = move_pan(list_x,start,end,deep,f)
        
    else :
        list_x = hanoi(list_x,num-1,start,mid,f,deep+1)
        
        list_x = move_pan(list_x,start,end,deep,f)
        
        list_x = hanoi(list_x,num-1,mid,end,f,deep+1)

    return list_x
    
# ------------------------------------------------
index=input('index : ')
index=int(index)

list_x = [[],[],[]]
for i in range(0,index):
    list_x[0].append(index-i)

lin0 =len(list_x[0])
deep_min = lin0
deep_list.append(0)
for i in range(lin0):
    cnt_list.append(0)
    deep_list.append(0)

with open('hanoi.txt','w') as f:

    f.write(f'{list_x[0]}, {list_x[1]}, {list_x[2]} \n')
    hanoi(list_x,len(list_x[0]),0,2,f)

    f.write(f'deep max : {deep_max} \n')
    f.write(f'deep min : {deep_min} \n')
    f.write(f'cnt_list : {cnt_list} \n')
    f.write(f'deep_list : {deep_list} \n')
    f.write(f'start_list : {start_list} \n')
    f.write(f'end_list : {end_list} \n')