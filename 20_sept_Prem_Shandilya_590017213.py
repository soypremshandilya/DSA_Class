# Prem Shandilya (590017213) - 20 Sept MCA B5

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)

    def _insert_node(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_node(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_node(node.right, data)

    def pre_order_traversal(self):
        self._pre_order_traversal(self.root)
        print()

    def _pre_order_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    def post_order_traversal(self):
        self._post_order_traversal(self.root)
        print()

    def _post_order_traversal(self, node):
        if node is not None:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.data, end=" ")

    def in_order_traversal(self):
        self._in_order_traversal(self.root)
        print()

    def _in_order_traversal(self, node):
        if node is not None:
            self._in_order_traversal(node.left)
            print(node.data, end=" ")
            self._in_order_traversal(node.right)

    def search_node(self, data):
        return self._search_node(self.root, data)

    def _search_node(self, node, data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self._search_node(node.left, data)
        else:
            return self._search_node(node.right, data)

    def find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete_node(self, data):
        self.root = self._delete_node(self.root, data)

    def _delete_node(self, node, data):
        if node is None:
            return node
        elif data < node.data:
            node.left = self._delete_node(node.left, data)
        elif data > node.data:
            node.right = self._delete_node(node.right, data)
        else:
            if node.left is None and node.right is None:
                del node
                return None
            elif node.left is None:
                temp = node
                node = node.right
                del temp
            elif node.right is None:
                temp = node
                node = node.left
                del temp
            else:
                temp = self.find_min_node(node.right)
                node.data = temp.data
                node.right = self._delete_node(node.right, temp.data)
        return node

bst = BST()

bst.insert_node(50)
bst.insert_node(30)
bst.insert_node(20)
bst.insert_node(40)
bst.insert_node(70)
bst.insert_node(60)
bst.insert_node(80)

print("Pre-order traversal:", end=" ")
bst.pre_order_traversal()

print("Post-order traversal:", end=" ")
bst.post_order_traversal()

print("In-order traversal:", end=" ")
bst.in_order_traversal()

search_data = 40
if bst.search_node(search_data):
    print(f"Node {search_data} found in the BST.")
else:
    print(f"Node {search_data} not found in the BST.")

delete_data = 20
bst.delete_node(delete_data)
print(f"Node {delete_data} deleted from the BST.")

print("Pre-order traversal after deletion:", end=" ")
bst.pre_order_traversal()