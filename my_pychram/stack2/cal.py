import sys
sys.stdin = open("cal_input.txt", "r")

def cal2(a,b,inc):
    if inc == '+':
        return (a + b)
    elif inc == '-':
        return (a - b)
    elif inc == '*':
        return (a * b)
    elif inc == '/':
        return (a / b)

for testcase in range(1,11):
    input()
    strx = input()
    stack = []
    stack_cal = []
    num_list = ['0','1','2','3','4','5','6','7','8','9','.']
    num = ''


    for c in strx:
        if c in num_list: # 숫자 만들기
            num+=c
            continue
        elif num:
            stack.append(float(num))
            num=''

        if c=='(':
            stack_cal.append(c)
        elif c==')':
            while 1:
                inc = stack_cal.pop()
                if inc=='(':
                    break
                else:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(cal2(a,b,inc))

        elif c=='*' or c=='/':
            if len(stack_cal) and (stack_cal[-1]=='*' or stack_cal[-1]=='/'):
                b = stack.pop()
                a = stack.pop()
                inc = stack_cal.pop()
                stack.append(cal2(a, b, inc))
            stack_cal.append(c)
        elif c=='-' or c=='+':
            if len(stack_cal) and stack_cal[-1]!='(':
                b = stack.pop()
                a = stack.pop()
                inc = stack_cal.pop()
                stack.append(cal2(a, b, inc))
            stack_cal.append(c)

    if num:
        stack.append(float(num))
        num=''
    while len(stack_cal):
        inc = stack_cal.pop()
        b = stack.pop()
        a = stack.pop()
        stack.append(cal2(a,b,inc))

    print(f"{testcase} {int(stack[0])}")