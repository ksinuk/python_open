import sys
sys.stdin = open("중위순회_input.txt","r")

def prints(table,n):
    if n>=len(table) or table[n]==0:
        return 0
    prints(table,2*n)
    print(table[n][0],end='')
    prints(table, 2 * n+1)


for __ in range(1,11):
    size = int(input())
    table = [0 for i in range(size+1)]
    for i in range(size):
        li = list(input().split())
        li[0] = int(li[0])
        if len(li)==3:
            li[2] = int(li[2])
            table[li[0]] = [li[1],li[2],0]
        elif len(li)==4:
            li[2] = int(li[2])
            li[3] = int(li[3])
            table[li[0]] = [li[1], li[2], li[3]]
        else:
            table[li[0]] = [li[1], 0, 0]

    print("#{} ".format(__),end ='')
    prints(table,1)
    print()




