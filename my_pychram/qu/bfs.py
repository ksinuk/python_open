node = 7
lines = [[1,2],[1,3],[2,4],[2,5],[4,6],[5,6],[6,7],[3,7]]

table = [[0 for i in range(node+1)] for i in range(node+1)]
out = []
for line in lines:
    table[line[0]][line[1]] = 1
    table[line[1]][line[0]] = 1
qu = [1]

while len(qu):
    temp = qu.pop(0)
    out.append(temp)
    for i in range(1,node+1):
        if table[temp][i] == 1:
            table[temp][i] = 0
            table[i][temp] = 0
            for j in range(1,node+1):
                table[j][i] = 0
            qu.append(i)

print(out)
