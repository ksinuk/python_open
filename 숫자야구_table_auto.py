import random
import sys 
sys.stdout = open("숫자야구_table_out.txt", "w")

debug = False

def check(out,innum,cnt):
    strike , ball = 0,0
    for i in range(4):
        if out[i] == innum[i]:
            strike+=1
        elif innum[i] in out:
            ball+=1
    
    result = [0,0,0]
    result[0] , result[1] , result[2] = strike , ball , strike+ball

    cnt[0]+=1
    return result

#---------------------------------------------------
def make_table():
    table = []
    for a in range(0,10):
        for b in range(0,10):
            if a==b:
                continue
            for c in range(0,10):
                if a==c or b==c:
                    continue
                for d in range(0,10):
                    if a!=d and b!=d and c!=d:
                        table.append([a,b,c,d])
    return table

def edit_table(table,now,result,size):
    idx = 0
    while idx < size:
        nums = table[idx]
        ball , strike = 0,0
        for i in range(0,4):
            if nums[i] == now[i]:
                strike+=1
            elif now[i] in nums:
                ball+=1
        if result[0]==strike and result[1]==ball:
            idx+=1
        else:
            table.pop(idx)
            size-=1
    return size

def max_index(li):
    size = len(li)
    index = 0
    num = -1
    for i in range(size):
        if li[i] > num:
            num = li[i]
            index = i
    return index

def tonum(li):
    return li[0]*1000+li[1]*100+li[2]*10+li[3]

#------------------------------------------------------------------------------------------
def next_pitch(table,size):
    next_table = [0 for i in range(10)]
    for nums in table:
        for i in range(4):
            next_table[nums[i]] +=1

    result = [0,0,0,0]
    for n in range(10):
        if next_table[n] >= next_table[result[0]]:
            result.insert(0,n)
            result.pop()
        elif next_table[n] >= next_table[result[1]]:
            result.insert(1,n)
            result.pop()
        elif next_table[n] >= next_table[result[2]]:
            result.insert(2,n)
            result.pop()
        elif next_table[n] >= next_table[result[3]]:
            result.insert(3,n)
            result.pop()

    cnt_out = [[0,0,0,0,result[0]],[0,0,0,0,result[1]],[0,0,0,0,result[2]],[0,0,0,0,result[3]]]
    for nums in table:
        for i in range(4):
            num = nums[i]
            if result[0] == num:
                cnt_out[0][i]+=1
            elif result[1] == num:
                cnt_out[1][i]+=1
            elif result[2] == num:
                cnt_out[2][i]+=1
            elif result[3] == num:
                cnt_out[3][i]+=1
    for _ in range(4):
        idx = max_index(cnt_out[0][0:4])
        cnt_out[idx] , cnt_out[0] = cnt_out[0] , cnt_out[idx]
    for i in range(4):
        cnt_out[i] = cnt_out[i][4]

    start,i = 0,0
    end = size-1
    result = tonum(result)
    while start < end and i<4:
        mid = (start+end)//2
        now = tonum(table[mid])
        if mid==start or now == result:
            out = table.pop(mid)
            return out
        elif now < result:
            start = mid
        else:
            end = mid
    
    out = table.pop(start)
    return out

#---------------------------------------------------
def auto_cal(out,table):
    cnt = [0]
    ok = [-1,-1,-1]
    final = '1234'
    size = 5040

    while ok[0]!=4 and size>0:
        final = next_pitch(table,size)
        size -= 1
        ok = check(out,final,cnt)
        size = edit_table(table,final,ok,size)
    

    print("final : {}".format(final))
    if ok[0]==4:
        print("perfact!")
    else:
        print("false~~")
    print("cnt : {}".format(cnt[0]))
    print("-------------------------")

    return cnt[0]

#---------------------------------------------------
table = make_table()
if debug == False:
    outs = table[:]
    cnts = {}
    for out in outs:
        print("out   : {}".format(out))
        cnt = auto_cal(out,table[:])
        temp = cnts.get(cnt)
        if cnts.get(cnt):
            cnts[cnt] += 1
        else:
            cnts[cnt] = 1
    print("bye bye ~~")

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
    cnt = auto_cal('0146',table)
#----------------------------------------------1405
# cnt = auto_cal('2958')



    
    
    