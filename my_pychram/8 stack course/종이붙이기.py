import sys
sys.stdin = open("종이붙이기_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):   
    cut = int(input()) # 입력받은 종이의 길이
    stack = [0]*(cut//10) # 가로 길이가 10이면 0, 20이면 1을 저장해둔다.
    stack_point = (cut//10)-1 #미리 가로길이 10인 종이로 채운다.
    lenbox = cut #넣어진 종이의 갯수
    out = 0 #출력값
    
    while stack_point>=0: 
        if lenbox < cut: #스텍에 있는 종이의 길이가 북족하면 길이가 10인 종이로 채운다.
            stack_point +=1
            stack[stack_point] = 0
            lenbox +=10
        else: #종이를 정확히 붙이거나 너무 많이 붙였다. 
            
            if lenbox == cut: # 종이를 빈틈없이 붙였다.
                temp = 1
                for i in stack[0:stack_point+1]: #가로 길이가 20인 종이의 종류는 2가지이다.
                    if i: #그러므로 경우의 수 : 2^길이가 20인의 종이의 개수이다.
                        temp = temp<<1 #temp*=2                
                out +=temp #결과값 저장
                
            if stack[stack_point] == 0: #종이를 1장 뺀다.
                lenbox -=10
            else:
                lenbox-=20
            stack_point-=1
            
            while stack_point>=0: #다음 경우의 수를 구한다.
                if stack[stack_point] == 0:
                    stack[stack_point]+=1
                    lenbox +=10
                    break
                else:
                    stack_point-=1
                    lenbox -=20
            else: # 더이상 찾아야 할 경우의 수가 없다.
                break
    
    print(f"#{test_case} {out}")

