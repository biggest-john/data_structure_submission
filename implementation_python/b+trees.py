class BPlusTreeNode:
  def __init__(self, leaf=False):
    self.leaf = leaf
    self.keys = []
    self.children = []

    self.next = None

class BPlusTree:
  def __init__(self, t):
    self.root = BPlusTreeNode(True)
    self.t = t

  def search(self, key, node=None):
      if node is None:
        node = self.root

      i = 0

      while i < len(node.keys) and key > node.keys[i]:
          i += 1

      if node.leaf:
        if i < len(node.keys) and node.keys[i] == key:
            return True
        return False
      return self.search(key, node.children[i])

  def insert(self, key):
    root = self.root

    if len(root.keys) == (2 * self.t) - 1:
        new_root = BPlusTreeNode(False)
        new_root.children.append(root)
        self.split_child(new_root, 0)
        self.root = new_root
        
    self.insert_non_full(self.root, key)


  def split_child(self, parent, index):

    t = self.t
    node = parent.children[index]
    new_node = BPlusTreeNode(node.leaf)
    mid = t - 1

    if node.leaf:
      new_node.keys = node.keys[mid:]
      node.keys = node.keys[:mid]

      
      new_node.next = node.next
      node.next = new_node

      parent.keys.insert(index, new_node.keys[0])
      parent.children.insert(index + 1, new_node)
    else:
      promote = node.keys[mid]
      new_node.keys = node.keys[mid + 1:]
      node.keys = node.keys[:mid]

      new_node.children = node.children[mid + 1:]
      node.children = node.children[:mid + 1]

      parent.keys.insert(index, promote)
      parent.children.insert(index + 1, new_node)


  def insert_non_full(self, node, key):
    i = len(node.keys) - 1

    if node.leaf:
      node.keys.append(None)
      while i >= 0 and key < node.keys[i]:
          node.keys[i + 1] = node.keys[i]
          i -= 1
      node.keys[i + 1] = key
    else:
      while i >= 0 and key < node.keys[i]:
          i -= 1
      i += 1
      child = node.children[i]

      if len(child.keys) == (2 * self.t) - 1:
          self.split_child(node, i)
          if key > node.keys[i]:
              i += 1
      self.insert_non_full(node.children[i], key)

  def display(self, node=None, level=0):
    if node is None:
        node = self.root
    print("Level", level, ":", node.keys)
    if not node.leaf:
        for child in node.children:
            self.display(child, level + 1)


  def traverse_leaves(self):
    current = self.root
    while not current.leaf:
        current = current.children[0]
    print("\nLeaf Nodes Linked List:")
    while current:
        print(current.keys, end=" -> ")
        current = current.next
    print("None")

bpt = BPlusTree(3)

values = [10, 20, 5, 6, 12, 30, 7, 17, 25, 40]

for v in values:
  bpt.insert(v)

print("B+ Tree Structure:\n")
bpt.display()

key = 25

if bpt.search(key):
  print(f"\n{key} found")
else:
  print(f"\n{key} not found")


bpt.traverse_leaves()