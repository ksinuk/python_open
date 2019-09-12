class Queue:
    def __init__(self,size=4):
        self.size = size
        self.Q = [0]*self.size
        self.start = 0
        self.end = 0

    def isFull(self):
        return ((self.end+1)%self.size == self.start)
    def isEmpty(self):
        return (self.end == self.start)
    def enQueue(self,item):
        if self.isFull():
            return "Q is Full"
        self.end = (self.end + 1)%self.size
        self.Q[self.end] = item
    def deQueue(self):
        if self.isEmpty():
            return "Q is Empty"
        self.start = (self.start + 1)%self.size
        return self.Q[self.start]
    def Qpeek(self):
        if self.isEmpty():
            return "Q is Empty"
        return self.Q[(self.start + 1)%self.size]

q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
print(q.Qpeek())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())



