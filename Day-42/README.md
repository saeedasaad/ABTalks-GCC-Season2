## Day-42: Number of Islands (Graph - DFS/BFS)

- **Grid Structure Used:**

```
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```

- **Problem Statement:**  
  Given a 2D grid of '1's (land) and '0's (water), return the number of **islands**.  
  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

- **Challenge Overview:**  
  - This challenge focuses on **graph traversal techniques** using DFS and BFS.  
  - The grid is treated as a graph where each cell is a node.  
  - Connected components of '1's represent islands.  
  - Time complexity is **O(m × n)** since each cell is visited once.  

- **Topics Covered:**  
  - Graph representation using grids  
  - Depth-First Search (DFS)  
  - Breadth-First Search (BFS)  
  - Connected components  
  - Matrix traversal  

- **Solution File:**  
  `solution.py`  

- **Approach:**  

  **DFS Approach:**
  - Traverse each cell in the grid.  
  - When a '1' is found, start DFS to mark the entire island.  
  - Recursively visit all adjacent cells (up, down, left, right).  
  - Increment island count.  

  **BFS Approach:**
  - Use a queue to explore neighbors level by level.  
  - Start BFS when a '1' is found.  
  - Mark visited cells as '0' to avoid revisiting.  

- **Example:**  
  - Input: Grid above  
  - Output: `3` islands  

- **Edge Cases Considered:**  
  - Empty grid → return 0  
  - Grid with all water → return 0  
  - Grid with all land → return 1  
  - Single cell grid  

- **Reflection:**  
  This challenge strengthened my understanding of **graph traversal in grid-based problems**.  
  I learned how DFS (recursion) and BFS (queue) can be used interchangeably to explore connected components.  
  The concept of islands is a classic pattern in coding interviews and applies to many real-world problems like **image processing and region detection**.  
  Practicing this improved my ability to visualize grids as graphs and solve problems efficiently.