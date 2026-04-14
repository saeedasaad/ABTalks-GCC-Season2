## Day-39: Maximum Depth of Binary Tree (Trees - Height)

- **Problem Statement:**  
  Given the root of a binary tree, return its **maximum depth**.  
  The maximum depth is defined as the number of nodes along the longest path from the root node to the farthest leaf node.

- **Challenge Overview:**  
  - This challenge focuses on understanding tree structures and how to measure their height.  
  - The solution uses **Depth-First Search (DFS)** with recursion to explore each branch.  
  - At every node, we compute the depth of left and right subtrees and take the maximum.  
  - Time complexity is **O(n)** since each node is visited once.  

- **Topics Covered:**  
  - Binary tree fundamentals  
  - Recursive problem solving  
  - Depth-First Search (DFS)  
  - Tree height calculation  
  - Handling edge cases (e.g., empty tree)  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  - If the root is `None`, return 0 (base case).  
  - Recursively compute the depth of the left subtree.  
  - Recursively compute the depth of the right subtree.  
  - Return `max(left_depth, right_depth) + 1`.  

- **Edge Cases Considered:**  
  - Empty tree → depth = 0  
  - Single node tree → depth = 1  
  - Skewed tree (like a linked list)  

- **Reflection:**  
  This challenge strengthened my understanding of **tree traversal and recursion**.  
  I learned how breaking a problem into smaller subproblems (left and right subtree depths) simplifies the solution.  
  The concept of tree height is crucial in many advanced algorithms such as **balanced trees, graph traversal, and search optimization**.  
  Practicing this problem improved my confidence in solving recursive problems and handling hierarchical data structures.