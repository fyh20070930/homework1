class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)    # 先访问根
        dfs(node.left)          # 再左子树
        dfs(node.right)         # 再右子树
    dfs(root)
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(preorderTraversal(root))
