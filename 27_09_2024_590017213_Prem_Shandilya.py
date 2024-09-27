class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def binary_tree_to_doubly(root):
    def convert_to_dll(node):
        nonlocal prev, head
        if not node:
            return
        convert_to_dll(node.left)

        if prev is None:
            head = node
        else:
            node.left = prev
            prev.right = node
        
        prev = node
        
        convert_to_dll(node.right)

    prev = None
    head = None
    
    convert_to_dll(root)
    
    return head

def print_dll(head):
    while head:
        print(head.data, end=" ")
        head = head.right
    print()

if __name__ == "__main__":
    root = Node(13)
    root.left = Node(7)
    root.right = Node(24)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(18)
    root.right.right = Node(28)
    
    dll_head = binary_tree_to_doubly(root)
    print("Doubly Linked List in sorted order:")
    print_dll(dll_head)
