import sys
sys.stdin = open("sample_input_unusally_sort.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    listx = list(map(int, input().split()))
    outlist = [0]*size
    out_index=0

    while 1:
        sum0=0
        one = -1
        for i in range(size):
            if listx[i]>-1:
                sum0+=1
                if one<0:
                    one = i
            if sum0>1:
                break
        if sum0==0:
            break
        if sum0==1:
            outlist[size-1]=listx[one]
            break

        min = one
        max = one
        for i in range(size):
            if listx[min] > listx[i] and listx[i]>-1:
                min = i
            if listx[max] < listx[i] and listx[i]>-1:
                max = i

        outlist[out_index] = listx[max]
        outlist[out_index+1] = listx[min]
        out_index+=2

        listx[max]=-1
        listx[min]=-1

    print(f"#{test_case}",end='')
    for i in range(10):
        print(f" {outlist[i]}",end='')
    print()