def atoi(strx):
    if type(strx)!=str:
        return 'error type'

    m=0
    while 1:
        if strx[m]=='-':
            m+=1
        else:
            break

    num = ['0','1','2','3','4','5','6','7','8','9']
    out=0
    for i in range(m,len(strx)):
        c= strx[i]
        if c not in num:
            return 'error'
        temp = num.index(c)
        out = out*10 + temp

    if m%2:
        return -out
    else:
        return out

def itoa(num):
    if type(num)!=int:
        return 'error type'

    numli = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    m=''
    if num<0:
        m='-'
        num= -num

    out=''
    while num>0:
        temp = num%10
        out = numli[temp] + out
        num //=10

    return m+out


a = "--12304"
inta = atoi(a)
print(inta, type(inta))
b= --12300455
strb = itoa(b)
print(strb, type(strb))

