## Day-40: Validate Binary Search Tree (Trees - Validation)

- **Problem Statement:**  
  Given the root of a binary tree, determine if it is a valid Binary Search Tree (BST).  
  A BST is defined as:
  - The left subtree of a node contains only nodes with values less than the node’s value.  
  - The right subtree contains only nodes with values greater than the node’s value.  
  - Both left and right subtrees must also be valid BSTs.  

- **Challenge Overview:**  
  - This challenge focuses on validating whether a binary tree satisfies BST properties.  
  - It requires understanding how constraints propagate through recursive calls.  
  - Instead of checking only immediate children, the algorithm ensures all nodes follow global constraints.  
  - The solution uses **Depth-First Search (DFS)** with value boundaries for correctness.  

- **Topics Covered:**  
  - Binary Search Tree (BST) properties  
  - Depth-First Search (DFS)  
  - Recursion with constraints (min/max range)  
  - Tree traversal techniques  
  - Edge case handling (null nodes, duplicates)  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  - Use a recursive helper function that keeps track of valid value ranges (`low`, `high`).  
  - For each node:
    - Ensure `low < node.val < high`  
    - Recursively validate:
      - Left subtree → range (`low`, node.val)  
      - Right subtree → range (`node.val`, high)  
  - If any node violates the constraint, return `False`.  

- **Time Complexity:**  
  **O(n)** — Each node is visited once  

- **Space Complexity:**  
  **O(h)** — Recursive stack space (height of the tree)  

- **Reflection:**  
  This challenge strengthened my understanding of how **global constraints** differ from local comparisons in tree problems.  
  Initially, it may seem sufficient to compare parent and child nodes, but a valid BST requires maintaining constraints across the entire subtree.  
  Implementing this using recursion improved my grasp of **DFS patterns** and **range-based validation techniques**.  
  This problem is highly relevant in technical interviews and demonstrates strong problem-solving skills in tree-based algorithms.