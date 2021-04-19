public class ListNode {
    int val;
    ListNode next;

    ListNode() {};

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    void printAll() {
        System.out.print(this.val + " ");
        if (this.next != null) {
            this.next.printAll();
        }
    }

    static ListNode createList(int[] args) {
        ListNode sentinel = new ListNode();
        ListNode head = sentinel;
        for (int i : args) {
            head.next = new ListNode(i);
            head = head.next;
        }
        return sentinel.next;
    }
}
