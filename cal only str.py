# 미완성

def my_sum(str1,str2):
    yn=''
    yx=''

    num1 = str1.split('.')
    num2 = str2.split('.')

    if len(num1)==2 or len(num2)==2:
        if len(num1)<2:
            num1.append('0')
        if len(num2)<2:
            num2.append('0') 

        len_decimal = 0
        if len(num1[1]) > len(num2[1]):
            len_decimal = len(num1[1])
        else :
            len_decimal = len(num2[1])
        yx1 = my_sum_n(num1[1],num2[1],1)
        prev = '0'
        if len(yx1)>len_decimal:
            i=1
            prev = yx1[0]
            while i<len(yx1):
                yx += yx1[i]
                i+=1
        else :
            yx=yx1

        yn = my_sum_n(num1[0],num2[0])
        yn = my_sum_n(yn,prev)

        return yn+'.'+yx
    else:
        return my_sum_n(num1[0],num2[0])

def my_sum_n(str1,str2,decimal=0):
    y=''

    if len(str1)<len(str2): # 자리수 맞추기
        str2 , str1 = str1 , str2
    if decimal:
        str2 = str2 + (len(str1)-len(str2))*'0'
    else :
        str2 = (len(str1)-len(str2))*'0'+str2
    
    list_num=['0','1','2','3','4','5','6','7','8','9']
    
    index_num = len(str1)-1
    prev = 0
    while index_num>=0:
        a=-1# 각 자리 수 알아내기
        for i in range(10):
            if list_num[i]==str1[index_num]:
                a=i
                break
        if a<0:
            return 'error'
        b=-1
        for i in range(10):
            if list_num[i]==str2[index_num]:
                b=i
                break
        if b<0:
            return 'error'
        
        c=a+b+prev # 자리 수 계산
        if c>=10: # 10이상의 수 념겨주기
            prev=1
            c-=10
        else :
            prev=0
        
        y = list_num[c] + y 
        
        index_num-=1
        
    if prev:
        y = list_num[1] + y
    
    return y


print(my_sum('3', '5'))
print(my_sum('123', '77'))
print(my_sum('0.1', '9999'))
print(my_sum('2.5', '5.5'))
print(my_sum('2.54', '2.004'))