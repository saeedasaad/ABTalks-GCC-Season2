## Day-31: Sort Colors (Software Engineering - Sorting)

- **Problem Statement:**  
  Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.  
  We use integers `0`, `1`, and `2` to represent the colors red, white, and blue respectively.  

- **Challenge Overview:**  
  - This is the classic **Dutch National Flag problem**.  
  - A naive approach would be to use Python’s built-in sort, but that gives `O(n log n)` complexity.  
  - The optimal solution uses **three pointers** (`low`, `mid`, `high`) to partition the array in a single pass.  
  - This ensures **O(n)** time complexity and **O(1)** space complexity.  

- **Topics Covered:**  
  - Sorting fundamentals  
  - Dutch National Flag algorithm  
  - In-place array manipulation  
  - Time complexity optimization (O(n))  
  - Interview-level problem solving  

- **Solution File:**  
  `solution.py`  

- **Reflection:**  
  This challenge reinforced the importance of **pointer-based sorting techniques**.  
  By applying the Dutch National Flag algorithm, I avoided multiple passes and achieved an efficient in-place solution.  
  The problem highlighted how sorting can be optimized beyond built-in functions, which is crucial for **real-world systems** like graphics rendering, scheduling, and memory management.  
  Practicing this problem improved my confidence in handling **array partitioning** and **in-place algorithms**, preparing me for interview-style coding challenges.  