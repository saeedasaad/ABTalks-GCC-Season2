class QueueUsingStacks:
    def __init__(self):

        self.in_stack = []

        self.out_stack = []

    def enqueue(self, x):
        """Add element to the end of the queue"""
        self.in_stack.append(x)

    def dequeue(self):
        """Remove element from the front of the queue"""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Dequeue from empty queue")
        return self.out_stack.pop()

    def peek(self):
        """Get the front element without removing it"""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Peek from empty queue")
        return self.out_stack[-1]

    def empty(self):
        """Check if the queue is empty"""
        return not self.in_stack and not self.out_stack



if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print(q.dequeue())  
    print(q.peek())     
    print(q.empty())    