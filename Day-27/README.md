## Day-27: Contains Duplicate II (Software Engineering - Hashing with dict/set)

- **Problem Statement:**  
  Given an integer array `nums` and an integer `k`, determine if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and the absolute difference between `i` and `j` is at most `k`.

- **Challenge Overview:**  
  - Hashing enables efficient duplicate detection by storing values in constant-time lookup structures.  
  - Using a dictionary (`dict`) or set allows us to track previously seen elements and their indices.  
  - The key insight is to check if a duplicate exists within the sliding window of size `k`.  
  - This problem is a common interview-style question testing knowledge of hashing, optimization, and edge-case handling.  

- **Topics Covered:**  
  - Hashing fundamentals  
  - Dictionary and set usage in Python  
  - Sliding window technique  
  - Optimizing time complexity with O(n) solutions  
  - Interview preparation for duplicate detection problems  

- **Solution File:**  
  `solution.py`  

- **Reflection:**  
  This challenge reinforced the importance of hashing for efficient duplicate detection. By storing indices in a dictionary, we avoided unnecessary nested loops and achieved an O(n) solution. The sliding window logic highlighted how constraints (`k`) can be integrated into hashing strategies. Practicing this problem improved my confidence in using dict/set for optimization and strengthened my readiness for interview-style coding challenges.