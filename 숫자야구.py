import random
num_list = ['0','1','2','3','4','5','6','7','8','9']

def make_num():
    out = [0,0,0,0]
    
    out[0] = random.choice(num_list)
    for i in range(1,4):
        out[i] = random.choice(num_list)
        while out[i] in out[0:i]:
            out[i] = random.choice(num_list)
    return out

def check(out,innum,cnt):
    strike , ball = 0,0
    for i in range(4):
        if out[i] == innum[i]:
            strike+=1
        elif innum[i] in out:
            ball+=1
    
    print("===============")
    print("strike : {}".format(strike))
    print("ball : {}".format(ball))
    print("===============")
    if strike==4:
        print("you win!")
        print("count : {}".format(cnt[0]))
        return 1
    
    cnt[0]+=1
    return 0
    
#---------------------------------------------------
out = make_num()
cnt = [0]

while 1:
    print("write 4 number : ",end="")
    instr = input()
    error = False
    if len(instr)!=4:
        print("input error : 숫자 4개를 입력하세요")
        continue
    for c in instr:
        if c not in num_list:
            print("input error : 숫자 만 입력하세요")
            error = True
            break
    if error:
        continue
    for i in range(4):
        if instr[i] in instr[0:i]:
            print("input error : 중복 된 수는 안됩니다.")
            error = True
            break
    if error:
        continue
    
    temp = check(out,instr,cnt)
    if temp!=0:
        break
    
    
    