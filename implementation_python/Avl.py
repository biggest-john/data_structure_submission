class Node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 1


class AVLTree:
  def get_height(self, node):
    if not node:
        return 0

    return node.height

  def get_balance(self, node):
    if not node:
        return 0

    return self.get_height(node.left) - self.get_height(node.right)

  def right_rotate(self, y):

    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(
        self.get_height(y.left),
        self.get_height(y.right)
    )

    x.height = 1 + max(
        self.get_height(x.left),
        self.get_height(x.right)
    )

    return x

  def left_rotate(self, x):

    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(
        self.get_height(x.left),
        self.get_height(x.right)
    )

    y.height = 1 + max(
        self.get_height(y.left),
        self.get_height(y.right)
    )

    return y

  def insert(self, root, key):

    if not root:
        return Node(key)

    elif key < root.data:
        root.left = self.insert(root.left, key)

    else:
        root.right = self.insert(root.right, key)

    root.height = 1 + max(
        self.get_height(root.left),
        self.get_height(root.right)
    )

    balance = self.get_balance(root)

    if balance > 1 and key < root.left.data:
        return self.right_rotate(root)

    if balance < -1 and key > root.right.data:
        return self.left_rotate(root)

    if balance > 1 and key > root.left.data:
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)

    if balance < -1 and key < root.right.data:
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)

    return root

  def get_min_value_node(self, root):

    if root is None or root.left is None:
      return root

    return self.get_min_value_node(root.left)

  def delete(self, root, key):
    if not root:
      return root
    elif key < root.data:
      root.left = self.delete(root.left, key)
    elif key > root.data:
      root.right = self.delete(root.right, key)
    else:
        if root.left is None:
          temp = root.right
          root = None
          return temp
        elif root.right is None:
          temp = root.left
          root = None
          return temp
          
        temp = self.get_min_value_node(root.right)

        root.data = temp.data

        root.right = self.delete(root.right, temp.data)

    if root is None:
      return root

    root.height = 1 + max(
      self.get_height(root.left),
      self.get_height(root.right)
    )

    balance = self.get_balance(root)

    if balance > 1 and self.get_balance(root.left) >= 0:
      return self.right_rotate(root)

    if balance > 1 and self.get_balance(root.left) < 0:
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)

    if balance < -1 and self.get_balance(root.right) <= 0:
      return self.left_rotate(root)

    if balance < -1 and self.get_balance(root.right) > 0:
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)

    return root

  def inorder(self, root):
    if root:
      self.inorder(root.left)
      print(root.data, end=" ")
      self.inorder(root.right)

  def display(self, root, level=0, prefix="Root: "):

    if root is not None:
      print(" " * (level * 4) + prefix + str(root.data))

      if root.left or root.right:
        self.display(root.left, level + 1, "L--- ")
        self.display(root.right, level + 1, "R--- ")



avl = AVLTree()

root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
  root = avl.insert(root, value)

print("AVL Tree Structure:\n")

avl.display(root)

print("\nInorder Traversal:")
avl.inorder(root)

print("\n\nDeleting 40...\n")

root = avl.delete(root, 40)

avl.display(root)