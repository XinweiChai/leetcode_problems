class Solution2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        boolean addOne = false;
        ListNode sumNode = new ListNode(), saveHead = sumNode;
        while (l1 != null || l2 != null || addOne) {
            sumNode.next = new ListNode(0);
            sumNode = sumNode.next;
            if (l1 != null) {
                sumNode.val += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                sumNode.val += l2.val;
                l2 = l2.next;
            }
            if (addOne) {
                sumNode.val += 1;
                addOne = false;
            }
            if (sumNode.val >= 10) {
                sumNode.val -= 10;
                addOne = true;
            }
        }
        return saveHead.next;
    }
}

public class problem2 {
    public static void main(String[] args) {
        Solution2 x = new Solution2();
        int[] a = { 2, 4, 3, 5 }, b = { 5, 6, 4 };
        x.addTwoNumbers(ListNode.createList(a), ListNode.createList(b)).printAll();
        System.out.println();
    }
}
