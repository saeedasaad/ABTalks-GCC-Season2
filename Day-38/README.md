## Day-38: Binary Tree Inorder Traversal (Tree Traversal - DFS)

- **Problem Statement:**  
  Given the root of a binary tree, return the inorder traversal of its nodes' values.

- **Challenge Overview:**  
  - This problem introduces **binary tree traversal**, specifically the **inorder traversal (Left → Root → Right)**.  
  - A simple recursive approach naturally follows the tree structure and is easy to implement.  
  - However, an iterative approach using a **stack** simulates recursion and is often asked in interviews.  
  - The goal is to visit nodes in a specific order while maintaining efficiency.  
  - Both approaches achieve **O(n)** time complexity, where `n` is the number of nodes.  

- **Topics Covered:**  
  - Binary Trees  
  - Depth-First Search (DFS)  
  - Recursion  
  - Stack-based traversal  
  - Tree data structures  

- **Solution File:**  
  `solution.py`  

- **Approach:**  

  **1. Recursive Approach:**  
  - Traverse the left subtree  
  - Visit the current node  
  - Traverse the right subtree  
  - This directly follows the definition of inorder traversal  

  **2. Iterative Approach:**  
  - Use a stack to simulate recursion  
  - Push all left nodes onto the stack  
  - Process nodes while moving to the right subtree  
  - Useful when recursion is not preferred  

- **Time & Space Complexity:**  
  - **Time Complexity:** `O(n)` (each node is visited once)  
  - **Space Complexity:**  
    - Recursive: `O(h)` (call stack, where `h` is tree height)  
    - Iterative: `O(h)` (stack usage)  

- **Reflection:**  
  This challenge helped me understand how **tree traversal works at a fundamental level**.  
  I learned how recursion naturally fits tree problems, making solutions clean and intuitive.  

  Implementing the iterative approach gave deeper insight into how recursion works behind the scenes using a **stack**.  
  This is especially useful in interviews where both recursive and iterative solutions may be required.  

  Mastering inorder traversal is important because it forms the basis for **Binary Search Trees (BSTs)**, where inorder traversal returns sorted values.  

  This problem strengthened my confidence in working with **hierarchical data structures**, which are widely used in file systems, databases, and search algorithms. 