def postOrder(node):
    if not node:
        return
    else:
        postOrder(node.left)
        postOrder(node.right)
        print(node.value, end=' ')

def preOrder(node):
    if not node:
        return
    else:
        print(node.value, end=' ')
        postOrder(node.left)
        postOrder(node.right)
def levelOrder(node):
    result = []
    result.append(node)
    while len(result) > 0:
        poped = result.pop(0)
        print(poped.value, end=' ')
        if poped.left:
            result.append(poped.left)
        if poped.right:
            result.append(poped.right)

    for t in range(len(result)-1, -1, -1):
        print(result[t], end=' ')