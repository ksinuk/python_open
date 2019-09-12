arr = [-3,3,-9,6,7,-6,1,5,4,-2]

plus = []
i=0
while i<len(arr):
    if arr[i]>0:
        plus.append(arr.pop(i))
    else:
        i+=1
m_l = len(arr)
p_l = len(plus)

out_num=0
for m_out in range(1,1<<m_l):
    for p_out in range(1,1<<p_l):
        sum=0
        mo = []
        po = []
        for mi in range(m_l):
            if m_out&(1<<mi):
                sum+=arr[mi]
                mo.append(arr[mi])
        for pi in range(p_l):
            if p_out&(1<<pi):
                sum+=plus[pi]
                po.append(plus[pi])
        if sum==0:
            out_num+=1
            print(mo,end='')
            print(po)
print(f"num : {out_num}")


