import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop() if self.s2 else None

    def peek(self):
        return self.s2[-1] if self.s2 else None

    def size(self):
        return len(self.s1) + len(self.s2)

    def isEmpty(self):
        return not self.s1 and not self.s2


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
