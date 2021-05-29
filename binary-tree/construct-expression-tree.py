import sys
import collections

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

def construct(postfix):
    stack = []

    for ch in postfix:
        if ch in '+-/x^':
            x = stack.pop()
            y = stack.pop()

            node = Node(ch, y, x)
            stack.append(node)
        else:
            stack.append(Node(ch))

    return stack[-1]

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

def inorder(root):
    if root:
        if root.data in '+-/x^':
            print("(", end=' ')
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
        if root.data in '+-/x^':
            print(")", end=' ')

if __name__ == '__main__':
 
    postfix = "ab+cde+xx"
    root = construct(postfix)
 
    print("Postfix Expression: ", end='')
    postorder(root)

    print("\nInfix Expression: ", end='')
    inorder(root)
 
