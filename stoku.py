import sys
sys.stdin = open("stoku_input.txt", "r")
sys.stdout = open("stoku_output.txt", "w")

def out_area9_index(main_table, x, y):
    x = (x//3)*3
    y = (y//3)*3
    return [[y,x], [y,x+1], [y,x+2], [y+1,x], [y+1,x+1], [y+1,x+2], [y+2,x], [y+2,x+1], [y+2,x+2]]

def input_num(main_table, y, x, num,stoku_cnt, isinput=False):
    if main_table[y][x]['ok'] and main_table[y][x]['out'] == num:
        return True
    elif main_table[y][x]['ok']:
        print("func inpu_num error : elif main_table[y][x]['ok']:")
        print("y: {} , x: {} , num: {} , table out : {}".format(y,x,num,main_table[y][x]['out']))
        return False
    elif not(isinput) and main_table[y][x]['nums'][num] != num:
        print("func inpu_num error : elif main_table[y][x]['nums'][num] != num:")
        print("y: {} , x: {} , num: {} , table out : {}".format(y,x,num,main_table[y][x]['out']))
        return False

    main_table[y][x]['ok'] = True
    main_table[y][x]['out'] = num
    stoku_cnt[0] += 1

    for n in range(10):
        main_table[y][x]['nums'][n] = -1

    for addr9 in out_area9_index(main_table, x, y):
        xx = addr9[1]
        yy = addr9[0]
        main_table[yy][xx]['nums'][num] = -1

    for i in range(9):
        main_table[i][x]['nums'][num] = -1
        main_table[y][i]['nums'][num] = -1

def check_table(main_table, stoku_cnt):
    for yy in range(3):
        for xx in range(3):
            cnt_num = [0 for i in range(10)]
            temp_table = [[-1, -1] for i in range(10)]
            for point in [[yy*3,xx*3], [yy*3,xx*3+1], [yy*3,xx*3+2], [yy*3+1,xx*3], [yy*3+1,xx*3+1], [yy*3+1,xx*3+2], [yy*3+2,xx*3], [yy*3+2,xx*3+1], [yy*3+2,xx*3+2]]:
                y = point[0]
                x = point[1]
                if main_table[y][x]['ok']:
                    continue
                for num in range(1,10):
                    if main_table[y][x]['nums'][num] == num:
                        cnt_num[num] += 1
                        temp_table[num] = [y,x]
            
            for num in range(1,10):
                y = temp_table[num][0]
                x = temp_table[num][1]
                if(cnt_num[num] == 1):
                    input_num(main_table, y, x, num, stoku_cnt)
    
    for yy in range(9):
        cnt_num = [0 for i in range(10)]
        temp_table = [[-1, -1] for i in range(10)]
        for point in range(9):
            y = yy
            x = point
            if main_table[y][x]['ok']:
                continue
            for num in range(1,10):
                if main_table[y][x]['nums'][num] == num:
                    cnt_num[num] += 1
                    temp_table[num] = [y,x]
        
        for num in range(1,10):
            y = temp_table[num][0]
            x = temp_table[num][1]
            if(cnt_num[num] == 1):
                input_num(main_table, y, x, num, stoku_cnt)

    for xx in range(9):
        cnt_num = [0 for i in range(10)]
        temp_table = [[-1, -1] for i in range(10)]
        for point in range(9):
            y = point
            x = xx
            if main_table[y][x]['ok']:
                continue
            for num in range(1,10):
                if main_table[y][x]['nums'][num] == num:
                    cnt_num[num] += 1
                    temp_table[num] = [y,x]
        
        for num in range(1,10):
            y = temp_table[num][0]
            x = temp_table[num][1]
            if cnt_num[num] == 1:
                input_num(main_table, y, x, num, stoku_cnt)

    for y in range(9):
        for x in range(9):
            cnt = 0
            in_num = -1
            for num in range(1,10):
                if main_table[y][x]['nums'][num] == num:
                    cnt += 1
                    in_num = num
            
            if cnt == 1:
                input_num(main_table, y, x, in_num, stoku_cnt)
#-------------------------------------------------------------------------------------------------------------------
def deepcopy_table(main_table):
    out_table = [ [ {'ok':False, 'out':-1, 'nums':[0,1,2,3,4,5,6,7,8,9]} for i in range(9)]  for j in range(9) ]
    for y in range(9):
        for x in range(9):
            out_table[y][x]['ok'] = main_table[y][x]['ok']
            out_table[y][x]['out'] = main_table[y][x]['out']
            for n in range(10):
                out_table[y][x]['nums'][n] = main_table[y][x]['nums'][n]
    return out_table

def check_error_table(main_table):
    for y in range(9):
        for x in range(9):
            if main_table[y][x]['ok']:
                now_num = main_table[y][x]['out']
                for i in range(9):
                    if main_table[y][i]['ok'] and i != x and main_table[y][i]['out'] == now_num:
                        return False
            else:
                error_cnt = 0
                for n in range(1,10):
                    if  main_table[y][x]['nums'][n] > 0:
                        error_cnt += 1
                if error_cnt == 0:
                    return False
    return True

def if_end_table(main_table):
    for y in range(9):
        for x in range(9):
            if not(main_table[y][x]['ok']):
                return False
    return True

def sort_table_list(main_table):
    outlist = []
    for y in range(9):
        for x in range(9):
            templist = main_table[y][x]['nums']
            cnt = 0
            for n in range(1,10):
                if main_table[y][x]['nums'][n] > 0:
                    cnt += 1
            outlist.push([y,x,cnt])
    
    step = 1
    point = 0
    while step < outlist.len:
        start_a = point
        start_b = end_a = point+step
        end_b = point+step*2 if point+step*2 < outlist.len else outlist.len
        
        


def backTracking(pre_table):
    main_table = deepcopy_table(pre_table)

# --------------------------------------------------------------------------------------------------------------

main_table = [ [ {'ok':False, 'out':-1, 'nums':[0,1,2,3,4,5,6,7,8,9]} for i in range(9)]  for j in range(9) ]

stoku_cnt = [0]
# input num in text -------------------------------------------------------------------
for y in range(9):
    line = list(input())
    orignNum = ['0','1','2','3','4','5','6','7','8','9']
    for x in range(9):
        if line[x] in orignNum:
            num = orignNum.index(line[x])
            input_num(main_table, y, x, num, stoku_cnt, True)


while stoku_cnt[0]:
    stoku_cnt[0] = 0
    check_table(main_table, stoku_cnt)
    check_table(main_table, stoku_cnt)

for y in range(9):
    print()
    if y%3==0 and y!=0:
        print()

    for x in range(9):
        if x%3==0 and x!=0:
            print(' ',end='')
        if not(main_table[y][x]['ok']):
            print(' ',end='')
        else:
            print(main_table[y][x]['out'],end='')


