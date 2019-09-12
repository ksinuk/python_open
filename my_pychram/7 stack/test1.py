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

#--------------------------
stack = Stack()
for i in range(1,211):
    stack.push(i)

for i in range(211):
    print(f"pop item : {stack.pop()}")