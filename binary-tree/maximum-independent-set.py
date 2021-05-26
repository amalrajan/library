import sys


try:
    sys.stdin = open(sys.path[0] + '/input.txt', 'r')
    sys.stdout = open(sys.path[0] + '/output.txt', 'w')
except FileNotFoundError:
    pass


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findMISSize(root, memo={}):
    if not root:
        return 0

    if root in memo:
        return memo[root]
    
    excl = findMISSize(root.left) + findMISSize(root.right)
    incl = 1

    if root.left:
        incl += (findMISSize(root.left.left) + findMISSize(root.left.right))
    if root.right:
        incl += (findMISSize(root.right.left) + findMISSize(root.right.right))

    memo[root] = max(incl, excl)
    return memo[root]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(findMISSize(root))
