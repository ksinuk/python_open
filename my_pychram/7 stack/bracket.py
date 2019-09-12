class Stack:
    def __init__(self):
        self.size = 100
        self.array = [0 for i in range(100)]
        self.top = -1

    def push(self,item):
        if self.top==99:
            self.size+=100
            temp = [0 for i in range(100)]
            self.array += temp
        self.top+=1
        self.array[self.top] = item

    def pop(self):
        if self.top==-1:
            return 'empty'
        out = self.array[self.top]
        self.top -=1
        return out
# -------------------------------------------

strx = '(5+6)*(5+7)*((5+6)*(4+5))'
dict_bracket = {')':'(' , '}':'{' , ']':'['}
stack = Stack()
for c in strx:
    if c=='(' or c=='{' or c=='[':
        stack.push(c)
    elif c==')' or c=='}' or c==']':
        temp = stack.pop()
        if temp!=dict_bracket[c]:
            print('error')
            break
else:
    if stack.pop()=='empty':
        print('ok')
    else:
        print('error')



