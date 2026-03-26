class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next


def build_linked_list(values):
    """Builds a linked list from a Python list and returns the head."""
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Prints linked list values in order."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))


if __name__ == "__main__":
    list1 = build_linked_list([1, 3, 5])
    list2 = build_linked_list([2, 4, 6])

    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)

    print("Merged Sorted List:")
    print_linked_list(merged_head)