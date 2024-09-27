public class Node {
    int data;
    Node left;
    Node right;

    public Node(int value) {
        data = value;
        left = null;
        right = null;
    }
}

public class BST {
    private Node root;

    private void _insertNode(Node node, int data) {
        if (data <= node.data) {
            if (node.left == null) {
                node.left = new Node(data);
            } else {
                _insertNode(node.left, data);
            }
        } else {
            if (node.right == null) {
                node.right = new Node(data);
            } else {
                _insertNode(node.right, data);
            }
        }
    }

    private void _preOrderTraversal(Node node) {
        if (node != null) {
            System.out.print(node.data + " ");
            _preOrderTraversal(node.left);
            _preOrderTraversal(node.right);
        }
    }

    private void _postOrderTraversal(Node node) {
        if (node != null) {
            _postOrderTraversal(node.left);
            _postOrderTraversal(node.right);
            System.out.print(node.data + " ");
        }
    }

    private void _inOrderTraversal(Node node) {
        if (node != null) {
            _inOrderTraversal(node.left);
            System.out.print(node.data + " ");
            _inOrderTraversal(node.right);
        }
    }

    private boolean _searchNode(Node node, int data) {
        if (node == null) {
            return false;
        } else if (node.data == data) {
            return true;
        } else if (data < node.data) {
            return _searchNode(node.left, data);
        } else {
            return _searchNode(node.right, data);
        }
    }

    private Node _findMinNode(Node node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    private Node _deleteNode(Node node, int data) {
        if (node == null) {
            return node;
        } else if (data < node.data) {
            node.left = _deleteNode(node.left, data);
        } else if (data > node.data) {
            node.right = _deleteNode(node.right, data);
        } else {
            if (node.left == null && node.right == null) {
                return null;
            } else if (node.left == null) {
                Node temp = node;
                node = node.right;
                temp = null;
            } else if (node.right == null) {
                Node temp = node;
                node = node.left;
                temp = null;
            } else {
                Node temp = _findMinNode(node.right);
                node.data = temp.data;
                node.right = _deleteNode(node.right, temp.data);
            }
        }
        return node;
    }

    public BST() {
        root = null;
    }

    public void insertNode(int data) {
        if (root == null) {
            root = new Node(data);
        } else {
            _insertNode(root, data);
        }
    }

    public void preOrderTraversal() {
        _preOrderTraversal(root);
        System.out.println();
    }

    public void postOrderTraversal() {
        _postOrderTraversal(root);
        System.out.println();
    }

    public void inOrderTraversal() {
        _inOrderTraversal(root);
        System.out.println();
    }

    public boolean searchNode(int data) {
        return _searchNode(root, data);
    }

    public void deleteNode(int data) {
        root = _deleteNode(root, data);
    }

    public static void main(String[] args) {
        BST bst = new BST();

        // Insert nodes into the BST
        bst.insertNode(50);
        bst.insertNode(30);
        bst.insertNode(20);
        bst.insertNode(40);
        bst.insertNode(70);
        bst.insertNode(60);
        bst.insertNode(80);

        // Perform traversals
        System.out.print("Pre-order traversal: ");
        bst.preOrderTraversal();

        System.out.print("Post-order traversal: ");
        bst.postOrderTraversal();

        System.out.print("In-order traversal: ");
        bst.inOrderTraversal();

        // Search for a node
        int searchData = 40;
        if (bst.searchNode(searchData)) {
            System.out.println("Node " + searchData + " found in the BST.");
        } else {
            System.out.println("Node " + searchData + " not found in the BST.");
        }

        // Delete a node
        int deleteData = 20;
        bst.deleteNode(deleteData);
        System.out.println("Node " + deleteData + " deleted from the BST.");

        // Perform traversals after deletion
        System.out.print("Pre-order traversal after deletion: ");
        bst.preOrderTraversal();
    }
}