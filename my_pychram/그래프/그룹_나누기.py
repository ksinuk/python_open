import sys
sys.stdin = open("그룹_나누기 _input.txt", "r")
#-----------------------------------------
def find_first(groups,x):
    if groups[x]==x:
        return x
    groups[x] = find_first(groups,groups[x])
    return groups[x]
#------------------------------------------
T = int(input())
for test_case in range(1, T + 1):
    students , num = map(int,input().split())
    votes = [0]*num

    inputs = list(map(int,input().split()))
    for i in range(0,num):
        votes[i] = [inputs[i*2],inputs[i*2+1]]
    del inputs
    #--------------------------------------------
    groups = [i for i in range(students+1)]
    for vote in votes:
        groups[find_first(groups,vote[1])] = find_first(groups,vote[0])

    for i in range(1,students+1):
        find_first(groups,i)

    groups.sort()
    cnt = 1
    for i in range(2,students+1):
        if groups[i-1]!=groups[i]:
            cnt+=1

    print("#{} {}".format(test_case,cnt))