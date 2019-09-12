import sys
sys.stdin = open("반나누기.txt","r")

testcase = int(input())
for __ in range(testcase):
    man_size , min_man , max_man = map(int,input().split())
    mans = list(map(int,input().split()))
    mans.sort()
    
    # 입력 완료 ----------------------------------------------
    if mans[0] ==mans[-1]:
        print("-1")
        continue

    man_size = len(mans)
    temp_ban = []
    i=0
    while man_size>0:
        if man_size==0:break
        temp_ban.append(1)
        temp_scroe = mans.pop(0)
        man_size -=1
        while man_size:
            if temp_scroe == mans[0]:
                temp_ban[i] += 1
                mans.pop(0)
                man_size -=1
            else:
                break
        i+=1
    if len(temp_ban)<3:
        print("-1")
        continue
    goto = 0
    for i in range(len(temp_ban)):
        if temp_ban[i] > max_man:
            goto = 1
            break
    if goto:
        print("-1")
        continue

    # 전처리 완료 -----------------------------
    out = 10000
    middle_size = len(temp_ban)
    temp_a = 0
    for a in range(middle_size+1):    
        if a:
            temp_a += temp_ban[a-1]
        if temp_a<min_man: continue
        if temp_a>max_man: break

        temp_b = 0
        for b in range(a,middle_size+1):
            if a!=b:
                temp_b += temp_ban[b-1] 
            if temp_b<min_man: continue
            if temp_b>max_man: break

            temp_c = 0
            for i in range(b,middle_size):
                temp_c += temp_ban[i]
            if temp_c>max_man or temp_c<min_man:
                continue

            temp_out = max([temp_a,temp_b,temp_c])
            temp_out -= min([temp_a,temp_b,temp_c])
            if out > temp_out:
                out = temp_out

    if out < 2000: print(out)
    else: print("-1")


    

            





