class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def print_inorder(self, node):
        if node is None:
            return
        self.print_inorder(node.left)
        print(node.data, end=' ')
        self.print_inorder(node.right)

    def print_preorder(self, node):
        if node is None:
            return
        self.print_preorder(node.left)
        print_preorder(node.right)
        self.print(node.data, end=' ')

    def print_postorder(self, node):
        if node is None:
            return
        self.print(node.data, end=' ')
        print_postorder(node.left)
        self.print_postorder(node.right)

    def mirror(self, node):
        if node is None:
            return

        self.mirror(node.left)
        self.mirror(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp


bt = BinaryTree()
bt.root = Node(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)

bt.print_inorder(bt.root)

print()

bt.mirror(bt.root)
bt.print_inorder(bt.root)

print()
