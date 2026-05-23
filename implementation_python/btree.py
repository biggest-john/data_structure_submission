class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    
    def search(self, node, key):

        i = 0

        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == key:
            return node

        if node.leaf:
            return None

        return self.search(node.children[i], key)

    def split_child(self, parent, index):

        t = self.t
        y = parent.children[index]
        z = BTreeNode(y.leaf)

        middle_key = y.keys[t - 1]

        z.keys = y.keys[t:]

        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        parent.children.insert(index + 1, z)

        parent.keys.insert(index, middle_key)

    def insert(self, key):

        root = self.root

        if len(root.keys) == (2 * self.t) - 1:

            new_root = BTreeNode(False)
            new_root.children.append(root)

            self.split_child(new_root, 0)

            self.root = new_root

            self.insert_non_full(new_root, key)

        else:
            self.insert_non_full(root, key)

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

            if len(node.children[i].keys) == (2 * self.t) - 1:

                self.split_child(node, i)

                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    def traverse(self, node):

        i = 0

        while i < len(node.keys):

            if not node.leaf:
                self.traverse(node.children[i])

            print(node.keys[i], end=" ")

            i += 1

        if not node.leaf:
            self.traverse(node.children[i])

    def delete(self, node, key):

        if key in node.keys:

            if node.leaf:
                node.keys.remove(key)
                print(f"Deleted {key}")
            else:
                print("Deletion from internal node not fully implemented.")
        else:
            if node.leaf:
                print(f"{key} not found.")
                return
            
            i = 0

            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            self.delete(node.children[i], key)

    def display(self, node, level=0):
        print("Level", level, ":", node.keys)

        if not node.leaf:
            for child in node.children:
                self.display(child, level + 1)

btree = BTree(3)

values = [10, 20, 5, 6, 12, 30, 7, 17]

for v in values:
    btree.insert(v)

print("B-Tree Structure:")
btree.display(btree.root)

print("\nTraversal:")
btree.traverse(btree.root)

print("\n")

key = 12

result = btree.search(btree.root, key)

if result:
    print(f"\n{key} found in B-Tree")
else:
    print(f"\n{key} not found")
