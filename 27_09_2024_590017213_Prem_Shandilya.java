class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int x) {
        val = x;
        left = right = null;
    }
}

class DoublyLinkedListNode {
    int val;
    DoublyLinkedListNode prev, next;

    DoublyLinkedListNode(int x) {
        val = x;
        prev = next = null;
    }
}

public class BSTToSortedCircularDLL {
    private DoublyLinkedListNode head = null;
    private DoublyLinkedListNode tail = null;

    public DoublyLinkedListNode convert(TreeNode root) {
        if (root == null) return null;

        inOrderTraversal(root);

        if (head != null && tail != null) {
            head.prev = tail;
            tail.next = head;
        }

        return head;
    }

    private void inOrderTraversal(TreeNode node) {
        if (node == null) return;

        inOrderTraversal(node.left);

        DoublyLinkedListNode newNode = new DoublyLinkedListNode(node.val);

        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }

        inOrderTraversal(node.right);
    }

    public void printList(DoublyLinkedListNode head) {
        if (head == null) return;

        DoublyLinkedListNode current = head;
        do {
            System.out.print(current.val + " ");
            current = current.next;
        } while (current != head);
        System.out.println();
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(6);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(3);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(7);

        BSTToSortedCircularDLL converter = new BSTToSortedCircularDLL();
        DoublyLinkedListNode head = converter.convert(root);
        converter.printList(head);
    }
}
