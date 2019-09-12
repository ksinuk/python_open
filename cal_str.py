# 미완성
def calc(strx,debug=0):
    if debug:
        print(f'strx : {strx}')

    operator_list = ['+','-','*','/']

    # 오류 정리
    if len(strx)>5 and strx[0:5]=="error":
        return strx
    if strx.count('(')!=strx.count(')'):
        return 'error : strx.count(\'(\')!=strx.count(\')\')'

    # 괄호 정리
    while ')' in strx:
        end = strx.index(')')
        start = end
        while strx[start]!='(':
            start-=1
            if start<0:
                return "error : don`t 1st \')\'"
        if start>0 and strx[start-1] not in operator_list :
            if strx[start-1]!='(':
                return "error : double operator"
        if end<len(strx)-1 and strx[end+1] not in operator_list :
            if strx[end+1]!=')':
                return "error : double operator"
        mid = calc(strx[start+1:end],debug)
        if mid[0:5]=="error":
            return mid
        strx = strx[0:start]+mid+strx[end+1:len(strx)]

    # 중복된 연산자 정리
    i=0
    while i<len(strx)-1:
        if strx[i]=='+':
            if strx[i+1]=='+' or strx[i+1]=='-':
                strx = strx[0:i]+strx[i+1:-1]
            elif strx[i+1]=='*' or strx[i+1]=='/':
                return 'error : double operator'
            else :
                i+=1
        elif strx[i]=='-':
            if strx[i+1]=='+':
                strx = strx[0:i+1]+strx[i+2:-1]
            elif strx[i+1]=='-':
                strx = strx[0:i]+'+'+strx[i+2:-1]
            elif strx[i+1]=='*' or strx[i+1]=='/':
                return 'error : double operator'
            else :
                i+=1
        else:
            i+=1

    # 초기화
    operator_stack=[]
    num_stack=[]
    if strx[0]=='+' or strx[0]=='-':
        num_stack.append(0)
        operator_stack.append(strx[0])
        strx=strx[1:len(strx)]
    elif strx[0]=='*' or strx[0]=='/':
        return 'error : 1st char is * or /'
    elif not(strx[0].isdecimal()):
        return 'error : not number and not op'

    # make stack
    temp = ''
    for c in strx:
        if c.isdecimal() or c=='.':
            temp+=c
        elif c=='*' or c=='/':
            if temp :
                num_stack.append(float(temp))
                temp=''
                operator_stack.append(c)
            else :
                return 'error : double operator'
        elif c=='+' or c=='-':
            if temp :
                num_stack.append(float(temp))
                temp=''
                operator_stack.append(c)
            else :
                temp+=c
        else :
            return 'error : not number and not operator'
    if temp:
        num_stack.append(float(temp))
        temp='' 
        
    # cal mul,div
    index=0
    while '*' in operator_stack or '/' in operator_stack:
        temp_op = operator_stack[index]
        if temp_op == '*':
            operator_stack.pop(index)
            temp_num = num_stack.pop(index+1)
            num_stack[index] *= temp_num
        elif temp_op == '/':
            operator_stack.pop(index)
            temp_num = num_stack.pop(index+1)
            num_stack[index] /= temp_num
        else :
            index+=1

    # cal add , sub
    out = num_stack.pop(0)
    
    while operator_stack and num_stack:
        num = num_stack.pop(0)
        operator = operator_stack.pop(0)
        
        if operator=='+':
            out +=num
        elif operator=='-':
            out -=num
        
    return str(out)

#--------------------------------
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('1+2*3+4'))
print(calc('1+2*(3+4)'))
print(calc('1+2*(3+4)*(3+2)*(3+2)'))
print(calc('1+2*(2+2*(1+1))'))
print(calc('1+2*(2+2*(1-3))'))