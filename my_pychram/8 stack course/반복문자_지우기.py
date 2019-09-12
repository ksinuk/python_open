import sys
sys.stdin = open("반복문자_지우기_input.txt", "r")

def mylen(lix): # 리스트의 길이를 출력
    out=0
    for c in lix:
        out +=1
    return out

#---------------------------
T = int(input())
for test_case in range(1, T + 1):
    lix = list(input()) #입력 문자열
    size = mylen(lix) #size = len(lix)
    
    while 1:
        n = size
        for i in range(n-1):
            if lix[i] == lix[i+1]: # 중복 지점 발견
                for j in range(i+2 , size): # 문자열 조정
                    lix[j-2] = lix[j]
                size = size-2   # 문자열 크기 조정
                break
        else: # 더이상 중복된 문자가 없음
            break
 
    print(f"#{test_case} {size}")