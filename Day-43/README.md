## Day-43: Flood Fill (Graph - BFS Traversal)

- **Problem Statement:**  
  Given a 2D grid representing an image, a starting pixel `(sr, sc)`, and a new color, perform a **flood fill** operation. Replace the original color of the starting pixel and all 4-directionally connected pixels of the same color with the new color.

---

- **Challenge Overview:**  
  - This challenge focuses on **graph traversal in grid-based problems** using BFS.  
  - Each cell in the grid is treated as a node in a graph.  
  - We explore all connected nodes (up, down, left, right) using a **queue-based BFS approach**.  
  - The algorithm ensures that all reachable cells of the same color are updated efficiently.  
  - Time complexity is **O(n × m)**, where n and m are grid dimensions.  

---

- **Topics Covered:**  
  - Grid-based graph representation  
  - Breadth-First Search (BFS)  
  - Queue data structure  
  - Visited state handling (via in-place marking)  
  - Boundary condition checks  
  - Connected components in graphs  

---

- **Solution File:**  
  `solution.py`

---

- **Approach:**  
  - Check if the starting cell already has the new color; if yes, return grid.  
  - Store the original color to identify which cells need to be replaced.  
  - Use a queue to perform BFS traversal from the starting cell.  
  - Explore all 4-directionally adjacent cells.  
  - If a neighbor matches the original color, update it and add it to the queue.  
  - Continue until all connected cells are processed.  

---

- **Edge Cases Considered:**  
  - Starting cell already has the new color  
  - Single-cell grid  
  - Entire grid has same color  
  - No valid connected component  
  - Large grid inputs  

---

- **Reflection:**  
  This problem strengthened my understanding of **BFS in grid-based graphs**.  
  It demonstrated how BFS can efficiently explore connected components level by level.  
  I also learned the importance of marking visited nodes early to avoid infinite loops.  
  Flood Fill is widely used in **image processing, game development, and region detection problems**, making it an important interview concept.