class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

d = Node('D', None, None)
e = Node('E', None, None)
f = Node('F', None, None)
b = Node('B', d, e)
c = Node('C', f, None)
root = Node('A', b, c)

def calc_height(root):
    if root is None:
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft,hRight) + 1

print(calc_height(root))

# 이진트리의 전위 순회
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

# 이진트리의 중위 순회
def inorder(n):
    if n is not None:
        preorder(n.left)
        print(n.data, end=' ')
        preorder(n.right)

# 이진트리의 후위 순회
def postorder(n):
    if n is not None:
        preorder(n.left)
        preorder(n.right)
        print(n.data, end=' ')

print('preorder: ', end='')
preorder(root)
print()
print('inorder: ', end='')
inorder(root)
print()
print('postorder: ', end='')
postorder(root)