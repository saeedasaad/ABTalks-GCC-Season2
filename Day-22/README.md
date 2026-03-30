 ### Day-22: Implement Queue using Stacks (Software Engineering - Deque)

- **Problem Statement:**  
  Implement a queue using two stacks. The queue should support the standard operations: enqueue (push) and dequeue (pop).  

- **Challenge Overview:**  
  - A queue follows FIFO (First-In-First-Out).  
  - A stack follows LIFO (Last-In-First-Out).  
  - By combining two stacks, we can simulate queue behavior.  
  - One stack (`in_stack`) is used for enqueue operations, while another (`out_stack`) is used for dequeue operations.  
  - When `out_stack` is empty, elements are transferred from `in_stack` to `out_stack` to maintain FIFO order.  

- **Topics Covered:**  
  - Queue fundamentals  
  - Stack fundamentals  
  - Logical transformation (FIFO using LIFO)  
  - Efficient data structure design  
  - Interview-style coding practice  

- **Solution File:**  
  `Day-22/solution.py`  

- **Reflection:**  
  This challenge reinforced how different data structures can be combined to achieve desired behavior. Implementing a queue using stacks highlights the importance of logical transformations in problem-solving. It also demonstrates how constraints can inspire creative solutions. Practicing this problem improved my ability to think about efficiency and transformations, which is crucial for system design and interviews.

  ---