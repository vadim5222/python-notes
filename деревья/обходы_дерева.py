## ============================== In-order(левый-корень-правый)
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

##=========================================Pre-order
def preorder(node):
    if node is None:
        return
    print(node.data)
    print(node.left)
    print(node.right)

##======================================= Post-order
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)