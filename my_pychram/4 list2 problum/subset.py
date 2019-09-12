import sys

def fact(n):
    out=1
    for i in range(1,n+1):
        out*=i
    return out

sys.stdin = open("sample_input_subset.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    num , sum_in = map(int, input().split())

    a_large = sum_in if sum_in<12 else 12

    out=0
    list_index = [1]*num
    for i in range(num):
        list_index[i] = 1

    cut= (fact(a_large)//(fact(num)))//fact(a_large-num)
    index = 0
    while index<cut:
        sum0 = 0
        now = 0
        for i in range(num):
            now += list_index[i]
            sum0 += now

        if sum0 == sum_in:
            out += 1

        for i in range(num):
            list_index[num-1-i] += 1
            sumif=0
            for j in range(num):
                sumif += list_index[j]
            if sumif <= a_large:
                break
            else:
                for j in range(i+1):
                    list_index[num-1-j] = 1
        index+=1


    print(f"#{test_case} {out}")
