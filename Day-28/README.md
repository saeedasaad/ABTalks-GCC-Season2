## Day-28: Two Sum (Software Engineering - Hashing with dict)

- **Problem Statement:**  
  Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`. Assume that each input has exactly one solution, and you may not use the same element twice.

- **Challenge Overview:**  
  - Hashing provides efficient lookup for complements when searching for pairs.  
  - Using a dictionary (`dict`) allows us to store previously seen numbers and their indices.  
  - The key insight is to check if the complement of the current number has already been seen.  
  - This problem is a classic interview-style question testing knowledge of hashing, optimization, and edge-case handling.  

- **Topics Covered:**  
  - Hashing fundamentals  
  - Dictionary usage in Python  
  - Complement-based lookup strategy  
  - Optimizing time complexity with O(n) solutions  
  - Interview preparation for pair-sum problems  

- **Solution File:**  
  `solution.py`  

- **Reflection:**  
  This challenge reinforced the power of dictionaries for constant-time lookups. By storing indices of previously seen numbers, we avoided nested loops and achieved an O(n) solution. The complement-checking logic highlighted how hashing can simplify pair-finding problems. Practicing this problem improved my confidence in using dicts for optimization and strengthened my readiness for interview-style coding challenges.