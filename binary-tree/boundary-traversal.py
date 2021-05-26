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

def leftBoundary(root):
    node = root

    while node and not (node.left is None and node.right is None):
        print(node.val, end=' ')
        
        if node.left:
            node = node.left
        else:
            node = node.right

def rightBoundary(root):
    while root and not (root.left is None and root.right is None):
        print(root.val, end=' ')

        if root.right:
            root = root.right
        else:
            root = root.left

def leafNodes(root):
    if not root:
        return

    if not root.left and not root.right:
        print(root.val, end=' ')
    
    leafNodes(root.left)
    leafNodes(root.right)

def performBoundaryTraversal(root):
    print(root.val, end=' ')

    leftBoundary(root.left)

    if root.left or root.right:
        leafNodes(root)

    rightBoundary(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.right = Node(10)
root.right.right.left = Node(11)
root.left.left.right.left = Node(12)
root.left.left.right.right = Node(13)
root.right.right.left.left = Node(14)

performBoundaryTraversal(root)
