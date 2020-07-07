import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def convert_expression(s, i):
    n = len(s)

    if i >= n:
        return None

    root = Node(s[i])
    i += 1

    if i < n and s[i] == '?':
        root.left = convert_expression(s, i + 1)
    elif i < n and s[i] == ':':
        root.right = convert_expression(s, i + 1)

    return root


def display(root):
    if root:
        print(root.val, end=' ')
        display(root.left)
        display(root.right)


expr = 'a?b?c:d:e'
root = convert_expression(expr, 0)
display(root)
