### Day-21: Daily Temperatures (Software Engineering - Monotonic Stack)

- **Problem Statement:**  
  Given an array of daily temperatures, return a new array where each element represents the number of days until a warmer temperature. If no warmer day exists, return 0 for that day.  

- **Challenge Overview:**  
  - Use a **monotonic decreasing stack** to efficiently solve the "next greater element" problem.  
  - Traverse the list of temperatures while maintaining indices in the stack.  
  - Pop indices when a warmer temperature is found and compute the difference.  
  - Push the current index onto the stack for future comparisons.  

- **Topics Covered:**  
  - Monotonic stack fundamentals  
  - Next greater element problems  
  - Optimizing time complexity to O(n)  
  - Stack-based problem-solving techniques  
  - Interview-style coding practice  

- **Solution File:**  
  `Day-21/solution.py`

- **Reflection:**  
  This challenge highlighted the power of monotonic stacks in solving "next greater element" problems. Instead of a brute-force O(n²) approach, the stack-based solution achieves O(n) efficiency by ensuring each index is pushed and popped at most once. It reinforced how stacks can be used not only for expression evaluation but also for sequence analysis. Practicing this problem improved my ability to recognize patterns where monotonic stacks apply, which is crucial for advanced interview preparation. It also reminded me how elegant data structures can transform seemingly complex problems into efficient solutions.

  ---