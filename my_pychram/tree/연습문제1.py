class Sample_Tree:
    def __init__(self,num=0,left=0,right=0,pre=0):
        self.pre = pre
        self.left = left
        self.right = right
        self.num = num

    def __str__(self):
        out = "{} : ".format(self.num)
        if self.left==0:
            out += "0 "
        else:
            out += "{} ".format(self.left.num)
        if self.right==0:
            out += "0 "
        else:
            out += "{} ".format(self.right.num)
        if self.pre==0:
            out += "0 "
        else:
            out += "{} ".format(self.pre.num)
        
        return out

def middle(now):
    if now==0:
        return 0
    middle(now.left)
    print(now.num,end=' ')
    middle(now.right)

def last(now):
    if now==0:
        return 0
    last(now.left)
    last(now.right)
    print(now.num,end=' ')


size = 13
lines = [[1,2],[1,3],[2,4],[3,5],[3,6],[4,7],[5,8],[5,9],[6,10],[6,11],[7,12],[11,13]]

table = [0 for i in range(size+1)]

now , left , right , pre = 0,0,0,0
for line in lines:
    a,b = line[0],line[1]
    if table[a]==0:
        table[a] = Sample_Tree(a,b,0,0)
        table[b] = Sample_Tree(b,0,0,table[a])
        table[a].left = table[b]
    elif table[a].left==0:
        table[b] = Sample_Tree(b,0,0,table[a])
        table[a].left = table[b]
    else:
        table[b] = Sample_Tree(b,0,0,table[a])
        table[a].right = table[b]

for i in range(len(table)):
    print(table[i])
        
stack = [table[1]]
while stack:
    temp = stack.pop()
    if temp==0:
        continue
    print(temp.num,end=' ')
    stack.append(temp.right)
    stack.append(temp.left)
print("\n----------------")
middle(table[1])
print("\n----------------")
last(table[1])

        


