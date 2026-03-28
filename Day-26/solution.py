class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None 

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)

sol = Solution()
print("Cycle start:", sol.detectCycle(head1))  

head2 = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node4 = ListNode(-4)

head2.next = node2
node2.next = node0
node0.next = node4
node4.next = node2 

cycle_start = sol.detectCycle(head2)
print("Cycle start:", cycle_start.val if cycle_start else None)  