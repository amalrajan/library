class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_inorder(root):
    if root:
        traverse_inorder(root.left)
        print(root.val, end=' ')
        traverse_inorder(root.right)


bt = TreeNode(1)
bt.left = TreeNode(2)
bt.right = TreeNode(3)
bt.left.left = TreeNode(4)
bt.left.right = TreeNode(5)

traverse_inorder(bt)
