class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    """
    Detects if a linked list has a cycle using Floyd's Cycle Detection Algorithm.
    
    Args:
        head (ListNode): Head node of the linked list.
    
    Returns:
        bool: True if cycle exists, False otherwise.
    """
    if not head or not head.next:
        return False
    
    slow, fast = head, head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True

if __name__ == "__main__":

    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 

    print("Cycle Detected:", hasCycle(node1))  