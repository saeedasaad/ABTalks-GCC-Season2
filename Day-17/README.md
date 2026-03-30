### Day-17: Climbing Stairs (Software Engineering - Dynamic Programming Introduction)

- **Problem Statement:**  
  You are climbing a staircase. It takes `n` steps to reach the top.  
  Each time you can climb either **1 step** or **2 steps**.  
  Write a program to determine how many distinct ways you can climb to the top.

- **Challenge Overview:**  
  - Explore how recursion can solve the problem but leads to repeated computations.  
  - Identify overlapping subproblems (e.g., ways to climb `n-1` and `n-2`).  
  - Apply **Dynamic Programming (DP)** to optimize the solution.  
  - Compare recursive vs DP approaches in terms of efficiency.  

- **Topics Covered:**  
  - Recursion fundamentals  
  - Overlapping subproblems  
  - Memoization (top-down DP)  
  - Tabulation (bottom-up DP)  
  - Time complexity improvement from exponential to linear  

- **Solution File:**  
  `Day-17/solution.py`

- **Reflection:**  
  This challenge demonstrated the transition from recursion to dynamic programming.  
  Initially, recursion provided a straightforward solution but was inefficient for large `n` due to repeated calculations.  
  By applying memoization and tabulation, I learned how DP eliminates redundancy and drastically improves performance.  
  This exercise reinforced the importance of recognizing overlapping subproblems and optimizing them—a key skill for advanced coding interviews.
---
