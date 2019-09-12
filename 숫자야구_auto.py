import random
import sys 
sys.stdout = open("숫자야구_out.txt", "w")

num_list = ['0','1','2','3','4','5','6','7','8','9']

debug = False

def make_num(pre):
    out = pre+1
    out_in = str(out)
    if len(out_in)<4:
        out_in = '0'*(4-len(out_in))+out_in
    strs = list(out_in)

    while strs[0]==strs[1] or strs[0]==strs[2] or strs[0]==strs[3] or strs[1]==strs[2] or strs[1]==strs[3] or strs[2]==strs[3]:
        out = out+1
        out_in = str(out)
        if len(out_in)<4:
            out_in = '0'*(4-len(out_in))+out_in
        strs = list(out_in)

        if out>9876:
            print("bye bye ~~")
            return -1
    
    print("out : {}".format(out))
    return out

def make_num_rand():
    out = [0,0,0,0]
    
    out[0] = random.choice(num_list)
    for i in range(1,4):
        out[i] = random.choice(num_list)
        while out[i] in out[0:i]:
            out[i] = random.choice(num_list)
    
    print("out : {}".format(out))
    return out

def check(out,innum,cnt,table,balls,final):
    strike , ball = 0,0
    for i in range(4):
        if out[i] == str(innum[i]):
            strike+=1
        elif str(innum[i]) in out:
            ball+=1
    
    result = [0,0,0]
    result[0] , result[1] , result[2] = strike , ball , strike+ball

    # print("===============")
    # print("innum  : {}".format(innum))
    # print("strike : {}".format(strike))
    # print("ball   : {}".format(ball))
    # print("===============")
    # if strike==4:
    #     print("you win!")
    #     print("count : {}".format(cnt[0]))

    table_num = list(map(int,innum[:]))

    now_strike = 0
    now_ball = 0
    for i in range(0,4):
        if table_num[i] == final[i] or table_num[i] in balls and table[table_num[i]][i] == 1:
            now_strike += 1
            final[i] = table_num[i]
            table[table_num[i]][i] = 1
        elif table_num[i] in balls:
            now_ball += 1

    if result[0]==now_strike:
        for i in range(0,4):
            if table[table_num[i]][i] != 1:
                table[table_num[i]][i] = -1
    elif result[1]==0:
        table[table_num[0]][0] = table[table_num[1]][1] = table[table_num[2]][2] = table[table_num[3]][3] = 1

    cnt[0]+=1
    return result

def make_from_balls(balls,nones,other):
    while other:
        other.pop()
    while nones:
        nones.pop()
    for i in range(10):
        if i not in balls:
            nones.append(i)


def printout(ok,cnt,final):
    print("final : {}".format(list(final)))
    if ok:
        print("perfact!")
    else:
        print("false~~")
    print("cnt : {}".format(cnt[0]))
    print("-------------------------")

    return cnt[0]

#---------------------------------------------------
def auto_cal(out):
    cnt = [0]
    strike_table = [[0,0,0,0] for i in range(10)]
    balls = []
    other = []
    nones = []
    final = [-1]*4

    result1234 = check(out,'1234',cnt,strike_table,balls,final)
    if result1234[0]==4:
        return printout(True,cnt,'1234')

    result5678 = check(out,'5678',cnt,strike_table,balls,final)
    if result5678[0]==4:
        return printout(True,cnt,'5678')

    if result1234[2]:
        result2190 = check(out,'2190',cnt,strike_table,balls,final)
        if result2190[0]==4:
            return printout(True,cnt,'2190')

    if result5678[2]:
        result6509 = check(out,'6509',cnt,strike_table,balls,final)
        if result6509[0]==4:
            return printout(True,cnt,'6509')

    temps = [0,0,0,0,0]
    temps[4] = 4-(result1234[2] + result5678[2])
    if result1234[2]:
        temps[0] = result2190[2] - temps[4]
        temps[1] = result1234[2] - temps[0]
    if result5678[2]:
        temps[2] = result6509[2] - temps[4]
        temps[3] = result5678[2] - temps[2]

    
    for i in range(5):
        if temps[i]==2:
            balls.append((i*2+1)%10)
            balls.append((i*2+2)%10)
        elif temps[i]==1:
            other.append([ (i*2+1)%10, (i*2+2)%10 ])
        else:
            nones.append((i*2+1)%10)
            nones.append((i*2+2)%10)
    
    tempin = []
    temp_1st = [0,0,0]
    if len(other)==4:
        tempin = [other[0][0] , other[1][0] , other[2][0] , other[3][0]]
        temp_1st = check(out,tempin,cnt,strike_table,balls,final)
        if temp_1st[0]==4:
            return printout(True,cnt,tempin)
        if temp_1st[2]==4:
            balls = tempin[:]
            make_from_balls(balls,nones,other)
        elif temp_1st[2]==0:
            balls = [other[0][1] , other[1][1] , other[2][1] , other[3][1]]
            make_from_balls(balls,nones,other)
        else:
            tempin = [other[0][1] , other[1][1] , other[2][0] , other[3][0]]
            temp_2nd = check(out,tempin,cnt,strike_table,balls,final)
            tempin = [other[0][0] , other[1][0] , other[2][0] , other[3][0]]
            if temp_2nd[0]==4:
                return printout(True,cnt,tempin)
            elif temp_2nd[2]==4:
                balls = [other[0][1] , other[1][1] , other[2][0] , other[3][0]]
                make_from_balls(balls,nones,other)
            elif temp_2nd[2]==0:
                balls = [other[0][0] , other[1][0] , other[2][1] , other[3][1]]
                make_from_balls(balls,nones,other)
            elif temp_1st[2] < temp_2nd[2]:
                balls = [other[0][1] , other[1][1]]
                nones.append(other[0][0])
                nones.append(other[1][0])
                other.pop(0)
                other.pop(0)
            elif temp_1st[2] > temp_2nd[2]:
                balls = [other[0][0] , other[1][0]]
                nones.append(other[0][1])
                nones.append(other[1][1])
                other.pop(0)
                other.pop(0)
            else:
                tempin = [other[0][1] , other[1][0] , other[2][0] , other[3][0]]
                temp_3rd = check(out,tempin,cnt,strike_table,balls,final)
                tempin = [other[0][0] , other[1][0] , other[2][0] , other[3][0]]
                if temp_3rd[0]==4:
                    return printout(True,cnt,tempin)
                elif temp_3rd[2]==4:
                    balls = [other[0][1] , other[1][0] , other[2][0] , other[3][0]]
                    make_from_balls(balls,nones,other)
                elif temp_3rd[2]==0:
                    balls = [other[0][0] , other[1][1] , other[2][1] , other[3][1]]
                    make_from_balls(balls,nones,other)
                elif temp_3rd[2] < temp_2nd[2] and temp_3rd[2]==2:
                    balls = [other[0][0] , other[1][1] , other[2][0] , other[3][0]]
                    make_from_balls(balls,nones,other)
                elif temp_3rd[2] > temp_2nd[2] and temp_3rd[2]==2:
                    balls = [other[0][1] , other[1][0] , other[2][1] , other[3][1]]
                    make_from_balls(balls,nones,other)
                elif temp_3rd[2] < temp_2nd[2]:
                    balls = [other[0][0] , other[1][1]]
                    nones.append(other[0][1])
                    nones.append(other[1][0])
                    other.pop(0)
                    other.pop(0)
                elif temp_3rd[2] > temp_2nd[2]:
                    balls = [other[0][1] , other[1][0]]
                    nones.append(other[0][0])
                    nones.append(other[1][1])
                    other.pop(0)
                    other.pop(0)


    if len(other)==2:
        tempin = [other[0][0] , other[1][0] , balls[0] , balls[1]]
        temp_1st = check(out,tempin,cnt,strike_table,balls,final)
        if temp_1st[0]==4:
            return printout(True,cnt,tempin)
        if temp_1st[2]==4:
            balls = tempin[:]
            make_from_balls(balls,nones,other)
        elif temp_1st[2]==2:
            balls = [other[0][1] , other[1][1] , balls[0] , balls[1]]
            make_from_balls(balls,nones,other)
        elif temp_1st[2]==3:
            tempin = [other[0][1] , other[1][0] , balls[0] , balls[1]]
            temp_2nd = check(out,tempin,cnt,strike_table,balls,final)
            if temp_2nd[0]==4:
                return printout(True,cnt,tempin)
            if temp_2nd[2]==4:
                balls = [other[0][1] , other[1][0] , balls[0] , balls[1]]
                make_from_balls(balls,nones,other)
            else:
                balls = [other[0][0] , other[1][1] , balls[0] , balls[1]]
                make_from_balls(balls,nones,other)

    tempin = nones[0:4]
    i = 0
    while i<len(balls): 
        if 1 in strike_table[balls[i]]:
            idx = strike_table[balls[i]].index(1)
            final[idx] = balls.pop(i)
        else:
            i+=1

    start , end = 0,3
    while start<4 and final[start]>=0:start+=1
    while end>=0 and final[end]>=0:end-=1
    while start < end:
        if final[start] >=0:
            start+=1
            continue
        for j in range(len(balls)-1):
            if strike_table[balls[j]][start] == -1:
                continue
            tempin[start] = balls[j]
            result = check(out,tempin,cnt,strike_table,balls,final)
            tempin[start] = nones[start]
            if result[0] != 0:
                final[start] = balls.pop(j)
                break
        else:
            final[start] = balls.pop()
        start+=1
    if end>=0 and balls:
        final[end] = balls.pop()

    ok = check(out,final,cnt,strike_table,balls,final)
    print("final : {}".format(final))
    if ok[0]==4:
        print("perfact!")
    else:
        print("false~~")
    print("cnt : {}".format(cnt[0]))
    print("-------------------------")

    return cnt[0]

#---------------------------------------------------
if debug == False:
    out = 123
    cnts = {}
    while out<=9876:
        out_in = str(out)
        if len(out_in)<4:
            out_in = '0'*(4-len(out_in))+out_in
        cnt = auto_cal(out_in)
        temp = cnts.get(cnt)
        if cnts.get(cnt):
            cnts[cnt] += 1
        else:
            cnts[cnt] = 1
        out = make_num(out)
        if out<0:break

    max_cnt = 0
    min_cnt = 9999999
    for cnt in cnts:
        if cnt < min_cnt:
            min_cnt = cnt
        if cnt > max_cnt:
            max_cnt = cnt
    for cnt in range(min_cnt,max_cnt+1):
        if cnts.get(cnt):
            print("cnt[{}] : {}".format(cnt,cnts[cnt]))
else:
    cnt = auto_cal('0146')
#----------------------------------------------1405
# cnt = auto_cal('2958')



    
    
    