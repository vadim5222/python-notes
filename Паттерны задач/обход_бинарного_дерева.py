def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result


def preorder(root):
    if not root: return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def postorder(root):
    if not root: return []
    return postorder(root.left) + postorder(root.right) + [root.val]
