## Day-41: Lowest Common Ancestor of BST (Trees - LCA)

- **Tree Structure Used:**`

```
    6
   / \
  2   8
 / \ / \
0  4 7  9
  / \
 3   5

 ```

- **Problem Statement:**  
  Given a Binary Search Tree (BST), find the **Lowest Common Ancestor (LCA)** of two given nodes.  
  The LCA is defined as the lowest node in the tree that has both nodes as descendants.

- **Challenge Overview:**  
  - This challenge focuses on leveraging **Binary Search Tree properties** to efficiently find the LCA.  
  - Instead of traversing the entire tree, we use value comparisons to decide the direction.  
  - The solution avoids unnecessary recursion and works efficiently using iteration.  
  - Time complexity is **O(h)** where *h* is the height of the tree.  

- **Topics Covered:**  
  - Binary Search Tree (BST) properties  
  - Lowest Common Ancestor (LCA)  
  - Iterative traversal  
  - Tree navigation using comparisons  
  - Optimized search techniques  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  - Start from the root node.  
  - If both nodes (`p` and `q`) are smaller than the current node → move left.  
  - If both nodes are greater than the current node → move right.  
  - Otherwise, the current node is the **Lowest Common Ancestor**.  

- **Example:**  
  - Input: `p = 2`, `q = 4`  
  - Output: `LCA = 2`  

- **Edge Cases Considered:**  
  - One node is the ancestor of the other  
  - Both nodes are on the same subtree  
  - Nodes are on different sides of the root  
  - Tree with only one node  

- **Reflection:**  
  This challenge improved my understanding of how **BST properties simplify complex problems**.  
  Instead of exploring all paths, we efficiently narrowed down the search using comparisons.  
  The concept of LCA is widely used in **tree-based algorithms, hierarchical data processing, and interview problems**.  
  Practicing this strengthened my ability to think **optimally and avoid brute-force approach