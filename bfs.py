class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Building this tree:
#         3
#        / \
#       9   20
#          /  \
#         15   7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

from collections import deque

def level_order(root):
    result = []
    queue = deque([root])
    while queue:
        l = len(queue)
        val = []
        for _ in range(l):
            node = queue.popleft()
            val.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(val)
    return result
print(level_order(root))