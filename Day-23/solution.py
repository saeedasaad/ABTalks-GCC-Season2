class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def reverse_recursive(self, node):
        if node is None or node.next is None:
            self.head = node
            return node
        rest = self.reverse_recursive(node.next)
        node.next.next = node
        node.next = None
        return rest



if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    print("Original Linked List:")
    ll.display()

    ll.reverse_iterative()
    print("Reversed Linked List (Iterative):")
    ll.display()

    ll.reverse_recursive(ll.head)
    print("Reversed Linked List (Recursive):")
    ll.display()