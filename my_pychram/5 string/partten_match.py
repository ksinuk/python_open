# 미완성

def brute_force(p,t):
    if len(t)<len(p):
        return -1

    for ti in range(len(t)-len(p)+1):
        for pi in range(len(p)):
            if t[ti+pi]!=p[pi]:
                break
        else:
            return ti
    return -1

def patten_match(p,t):
    if len(t)<len(p) or len(p)==0:
        return -1
    elif len(p)==1:
        for i in range(len(t)):
            if t[i]==p:
                return i
        return -1

    p_li = {}
    for i in range(len(p)):
        c = p[i]
        p_li[c] = len(p)-i-1
    # p_li[p[-1]] = 1

    ti=0
    pi=0
    while ti <= len(t) - len(p):
        now_ti = ti + len(p) - 1
        while pi < len(p):
            if t[now_ti-pi]!=p[len(p)-1-pi]:
                if t[now_ti-pi] not in p_li:
                    ti += len(p)-pi
                else:
                    if t[now_ti] in p_li:
                        if p_li[t[now_ti]]>1:
                            ti = p_li[t[now_ti]]
                        else:
                            ti +=1
                    else:
                        ti+=1



                    # pp = p_li[t[now_ti-pi]]
                    # if pp>pi:
                    #     ti = ti + pp-pi
                    # else:
                    #     ti = ti+1
                break
            elif pi+1==len(p):
                return ti
            else:
                pi+=1
    return -1

t = "a pattern matching algorithm"
t = "roithm a pattern hmatching algorithm"
p = "rithm"
print(brute_force(p,t))
print(patten_match(p,t))