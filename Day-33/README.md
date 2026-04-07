## Day-33: First Bad Version (Software Engineering – Binary Search Variants)

- **Problem Statement:** 

   You are given `n` versions `[1, 2, ..., n]` and an API `isBadVersion   (version)` which returns whether a version is bad.  
   Your task is to find the **first bad version** while minimizing the number    of API calls.

- **Challenge Overview:**  

  - This problem is a **binary search variant** focusing on **boundary detection**.  
  - If a version is bad, continue searching **left** to ensure it’s the first bad version.  
  - If a version is good, the first bad version must be **after it**.  
  - Efficiently solved in **O(log n)** time.

- **Skills Practiced:**

  - Binary search variations  
  - Boundary condition handling  
  - Optimization techniques  
  - Logical problem solving  

- **Topics Covered:**  

  - Binary search fundamentals  
  - First/last occurrence detection  
  - Minimizing API calls  
  - Handling edge cases  

- **Solution File:** 
 
  `solution.py`


- **Reflection:**  

      - This challenge reinforced the **binary search beyond simple value search**.  
      - Handling boundaries is key — using `right = mid` ensures the **first bad version is not skipped**.  
      - Practicing this improves skills for **first/last occurrence problems** often asked in coding interviews.  
      - Minimizing API calls simulates **real-world constraints**, emphasizing efficiency.  
      - Using simple variable names like `num1`, `num2`, `num3` keeps the solution **readable and maintainable**.