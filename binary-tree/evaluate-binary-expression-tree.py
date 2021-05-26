import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def calc(op, x, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y

def evaluate(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return int(root.val)

    x = evaluate(root.left)
    y = evaluate(root.right)

    return calc(root.val, x, y)


root = Node('+')
root.left = Node('*')
root.right = Node('/')
root.left.left = Node('-')
root.left.right = Node('5')
root.right.left = Node('21')
root.right.right = Node('7')
root.left.left.left = Node('10')
root.left.left.right = Node('5')

print(evaluate(root))
