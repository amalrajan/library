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

def preorder(root):
    if not root:
        return
    
    print(root.val, end=' ')
    preorder(root.left)
    preorder(root.right)

def findChildrenSum(root):
    left = root.left.val if root.left else 0
    right = root.right.val if root.right else 0
    return left + right

def fixBinaryTree(root):
    if not root or not root.left or not root.right:
        return

    fixBinaryTree(root.left)
    fixBinaryTree(root.right)

    diff = root.val - findChildrenSum(root)

    if diff < 0:
        root.val += abs(diff)
    else:
        subtree = root.left if root.left else root.right
        subtree.val += diff
        fixBinaryTree(subtree)

root = Node(25)
root.left = Node(8)
root.right = Node(10)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preorder(root)
print()
fixBinaryTree(root)
preorder(root)
