count = 0 # 옮긴 횟수
deep_max = -1 # 저장된 함수의 최대 갯수
deep_min = 0  # 저장된 함수의 최초 갯수
cnt_list = [] # 각각의 수가 옮겨진 횟수
deep_list = [] # 각각의 깊이에 실행 된 함수의 갯수
from_this = [0,0,0] # 시작 지점 횟수
to_this = [0,0,0] # 종료 지점 횟수

from_to = [[0,0,0],[0,0,0],[0,0,0]]

statistic_count = [] 
statistic_deep_max = []
statistic_deep_min = []
statistic_cnt_list = []
statistic_deep_list = []
statistic_from_this = []
statistic_to_this = []

statistic_from_to = []

def move_pan(list_x,start,end,deep,f):
    global count , deep_max , deep_min , from_this , from_to
    global to_this , deep_list , cnt_list

    temp = list_x[start].pop()
    list_x[end].append(temp)

    count+=1
    cnt_list[temp-1]+=1
    from_this[start]+=1
    to_this[end]+=1
    from_to[start][end]+=1

    return list_x
# ----------------------------------------------------------
def hanoi(list_x,num,start,end,f,deep=1):
    if start == end :
        print('start == end error')
        return 'error'
    if len(list_x[start])<num:
        print('len(list_x[start])<num error')
        return 'error'
    
    # ----------------------------------------------------------
    global count , deep_max , deep_min , from_this , from_to
    global to_this , deep_list , cnt_list

    if deep_max < deep:
        deep_max = deep
    if deep_min > deep:
        deep_min = deep
    deep_list[deep] +=1
    
    # ----------------------------------------------------------
    mid = 3-start-end
    
    if num==1:
        list_x = move_pan(list_x,start,end,deep,f)
        
    else :
        list_x = hanoi(list_x,num-1,start,mid,f,deep+1)
        
        list_x = move_pan(list_x,start,end,deep,f)
        
        list_x = hanoi(list_x,num-1,mid,end,f,deep+1)

    return list_x
# --------- 함수 종료 ---------------------------------------    
# ------------------------------------------------
num=input('num : ')
num = int(num)

# ------------------------------------------------
with open('hanoi_statistics.txt','w') as f:
    for index in range(1,num+1):
        # 초기화
        count=0
        deep_max = -1
        cnt_list = []
        deep_list = []
        from_this = [0,0,0]
        to_this = [0,0,0]
        from_to = [[0,0,0],[0,0,0],[0,0,0]]

        f.write(f'{index}층 하노이 탑 통계 \n')
        list_x = [[],[],[]]
        for i in range(0,index):
            list_x[0].append(index-i)

        lin0 =len(list_x[0])
        deep_min = lin0
        deep_list.append(0)
        for i in range(lin0):
            cnt_list.append(0)
            deep_list.append(0)

        hanoi(list_x,lin0,0,2,f)

        f.write(f'count : {count} \n')
        statistic_count.append(count)
        f.write(f'deep max : {deep_max} \n')
        statistic_deep_max.append(deep_max)
        f.write(f'deep min : {deep_min} \n')
        statistic_deep_min.append(deep_min)
        f.write(f'cnt_list : {cnt_list} \n')
        statistic_cnt_list.append(cnt_list)
        f.write(f'deep_list : {deep_list} \n')
        statistic_deep_list.append(deep_list)
        f.write(f'from_this : {from_this} \n')
        statistic_from_this.append(from_this)
        f.write(f'to_this : {to_this} \n')
        statistic_to_this.append(to_this)

        f.write(f'a_to : {from_to[0]} \n')
        f.write(f'b_to : {from_to[1]} \n')
        f.write(f'c_to : {from_to[2]} \n')
        statistic_from_to.append(from_to)


        f.write('-----------------------------------------------\n')
    
    f.write(f'statistic_count \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_count[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_deep_max \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_deep_max[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_deep_min \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_deep_min[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_cnt_list \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_cnt_list[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_deep_list \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_deep_list[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_from_this \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_from_this[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_to_this \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_to_this[index]} \n')
    f.write('-----------------------------------------------\n')   
    f.write(f'statistic_from_to \n')
    for index in range(0,num):
        f.write(f'{index+1:2} : {statistic_from_to[index]} \n')