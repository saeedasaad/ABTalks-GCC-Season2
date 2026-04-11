## Day-37: Assign Cookies (Software Engineering - Greedy Approach)

- **Problem Statement:**  
  You are given two arrays:  
  - `g` representing the greed factor of children  
  - `s` representing the sizes of cookies  

  Each child can be assigned at most one cookie.  
  A child will be satisfied if the cookie size is greater than or equal to their greed factor.  

  The goal is to maximize the number of satisfied children.

- **Challenge Overview:**  
  - This problem demonstrates the power of the **Greedy Algorithm**.  
  - The idea is to always satisfy the least greedy child first using the smallest available cookie.  
  - By making locally optimal choices, we achieve a globally optimal solution.  
  - Sorting helps efficiently match children with appropriate cookies.  
  - Time complexity is **O(n log n)** due to sorting.

- **Topics Covered:**  
  - Greedy algorithm fundamentals  
  - Sorting for optimization  
  - Two-pointer technique  
  - Efficient decision-making strategies  
  - Edge case handling (empty arrays, insufficient cookies)

- **Solution File:**  
  `solution.py`

- **Reflection:**  
  This challenge helped me understand how **Greedy strategies** work in decision-making problems.  
  By prioritizing the smallest valid assignment, I ensured maximum utilization of resources.  
  It reinforced the importance of **sorting and two-pointer techniques** in optimization problems.  
  This problem is highly relevant in interviews and real-world scenarios where resource allocation is required.  
  Practicing this improved my ability to think **efficiently and strategically** while writing clean and optimal code.