import sys
sys.stdin = open("괄호검사_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    strx = input() # 문자열 입력
    stack = ['']*50
    index = -1 # 스텍의 마지막 위치
    out = 1 # 출력값
    
    for c in strx:
        if c=='(' or c=='{': # 여는 괄호를 스텍에 저장
            index+=1
            stack[index]=c
        elif c==')': # 닫는 괄호 확인
            if stack[index]=='(':
                index-=1
            else: # 문제점 발견시 출력값은 0 , 루프 종료
                out=0
                break
        elif c=='}': # 중괄호
            if stack[index]=='{':
                index-=1
            else:
                out=0
                break
    
    if index>=0: # 여는 괄호가 남았을 경우 출력값은 0
        out=0
    
    print(f"#{test_case} {out}")
