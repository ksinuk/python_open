import sys
sys.stdin = open("test3_input.txt")

class Stack:
    size = 100
    def __init__(self):
        self.size = Stack.size
        self.array = [0] * self.size
        self.top = -1

    def push(self, item):
        if self.top >= self.size-1:
            temp = [0] * Stack.size
            self.array += temp
            self.size += Stack.size
        self.top += 1
        self.array[self.top]=item

    def pop(self):
        if self.top<0:
            return 'empty'
        out = self.array[self.top]
        self.top -=1
        return out

    def __repr__(self):
        temp = list(map(str, self.array[0:self.top+1]))
        return f"[{' , '.join(temp)}]"

    def len(self):
        return self.top+1

#--------------------------

def dfs(start):
    out = Stack()
    stack = Stack()
    stack.push(start)

    while stack.len():
        print(stack, visited, out)
        now = stack.pop()
        if visited[now]:
            continue

        out.push(now)
        visited[now] = now
        for i in range(1, node_num + 1):
            if i != now and visited[i] == 0 and matrix[now - 1][i - 1]:
                stack.push(i)

    print('---------------------')
    return out

#--------------------------

node_num, edge_num = map(int , input().split())
temp = list(map(int , input().split()))

matrix = [[0 for i in range(node_num)] for j in range(node_num)] # matrix[node_num+1][node_num+1] = {0}
visited = [0 for i in range(node_num+1)]

for i in range(edge_num):
    matrix[temp[2*i]-1][temp[2*i+1]-1] = 1
    matrix[temp[2*i+1]-1][temp[2*i]-1] = 1

for li in matrix:
    print(li)
print('---------------------')

print(dfs(1))

