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

    if not node:
        return
    else:
        result.append(node)
        levelOrder(node.left)
        levelOrder(node.right)

for t in range(len(result)-1, -1, -1):
    print(result[t], end=' ')