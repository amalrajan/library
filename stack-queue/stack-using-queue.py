import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, val):
        self.q1.append(val)

    def pop(self):
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        res = self.q1.pop(0) if self.q1 else None
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self):
        if not self.q1:
            return None
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        
        res = self.q1.pop(0) if self.q1 else None
        self.q1, self.q2 = self.q2, self.q1
        return res

    def size(self):
        return len(self.q1) + len(self.q2)


s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
