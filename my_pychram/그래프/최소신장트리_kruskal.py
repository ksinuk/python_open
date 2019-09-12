import sys
sys.stdin = open("최소신장트리.txt", "r")

T = int(input())
def sort_line(lines,size):
    step = 1
    now = 0

    while step<size:
        a,ar,b,br = now,now+step,now+step,now+2*step
        br = size if size<br else br

        qu = []
        while a<ar and b<br:
            if lines[a][2] < lines[b][2]:
                qu.append(lines[a])
                a+=1
            else:
                qu.append(lines[b])
                b+=1
        while a<ar:
            qu.append(lines[a])
            a+=1
        while b<br:
            qu.append(lines[b])
            b+=1
        for i in range(len(qu)):
            lines[now+i] = qu[i]
        
        now+=2*step
        if now+step>=size:
            now = 0
            step *= 2

def find_set(sets,elec):
    if sets[elec]==elec:
        return elec
    sets[elec] = find_set(sets,sets[elec])
    return sets[elec]

for test_case in range(1, T + 1):
    nodes,size = map(int,input().split())
    lines = [[0,0,0] for i in range(size)]
    for i in range(size):
        lines[i] = list(map(int,input().split()))
    #----------------------------------------------
    sort_line(lines,size)
    #----------------------------------------------
    out = 0

    sets = [i for i in range(nodes+1)]
    for line in lines:
        if find_set(sets,line[0]) != find_set(sets,line[1]):
            sets[sets[line[1]]] = sets[sets[line[0]]]
            out += line[2]

    #-----------------------------------------------    
    print("#{} {}".format(test_case,out))
    

