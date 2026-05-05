## Day-55: Mixed Medium Problems (Software Engineering – Revision)

---

### Problem 1: Two Sum (HashMap Approach)

- **Problem Statement:**  
  Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

- **Challenge Overview:**  
  - Use a hash map to store complements.  
  - Efficiently check if the required pair exists.  
  - Avoid nested loops for optimization.  
  - Time complexity is **O(n)**.  

- **Topics Covered:**  
  - Hashing  
  - Dictionary lookups  
  - Array traversal  

- **Solution File:**  
  `solution.py`

- **Reflection:**  
  This problem reinforced the importance of **hash maps** in reducing time complexity. It showed how preprocessing complements can eliminate redundant checks and optimize performance.

---

### Problem 2: Longest Substring Without Repeating Characters

- **Problem Statement:**  
  Given a string `s`, find the length of the longest substring without repeating characters.

- **Challenge Overview:**  
  - Apply the sliding window technique.  
  - Expand and shrink the window to maintain uniqueness.  
  - Time complexity is **O(n)**.  

- **Topics Covered:**  
  - Sliding window  
  - HashSet usage  
  - String traversal  

- **Solution File:**  
  `solution.py`

- **Reflection:**  
  Practicing this problem improved my ability to use **two-pointer techniques** and manage dynamic windows efficiently. It highlighted how sliding window optimizations are crucial in string problems.

---

### Problem 3: Product of Array Except Self

- **Problem Statement:**  
  Given an integer array `nums`, return an array `output` such that `output[i]` is the product of all elements except `nums[i]`.

- **Challenge Overview:**  
  - Use prefix and suffix arrays.  
  - Avoid division to handle zeros.  
  - Time complexity is **O(n)**.  

- **Topics Covered:**  
  - Prefix & suffix logic  
  - Array preprocessing  
  - Space optimization  

- **Solution File:**  
  `solution.py`

- **Reflection:**  
  This problem strengthened my understanding of **array preprocessing**. It showed how prefix/suffix logic can solve problems without division, making solutions more robust.

---

### Problem 4: Search in Rotated Sorted Array

- **Problem Statement:**  
  Given a rotated sorted array and a target value, return its index if found, otherwise return -1.

- **Challenge Overview:**  
  - Use modified binary search.  
  - Identify sorted half and reduce search space.  
  - Time complexity is **O(log n)**.  

- **Topics Covered:**  
  - Binary search variations  
  - Rotated arrays  
  - Edge case handling  

- **Solution File:**  
  `solution.py`

- **Reflection:**  
  This problem highlighted the adaptability of **binary search**. It taught me how to handle rotated arrays and efficiently narrow down search ranges.

---

### Problem 5: Maximum Subarray (Kadane’s Algorithm)

- **Problem Statement:**  
  Given an integer array `nums`, find the contiguous subarray with the largest sum.

- **Challenge Overview:**  
  - Apply Kadane’s algorithm.  
  - Track maximum sum ending at each index.  
  - Time complexity is **O(n)**.  

- **Topics Covered:**  
  - Dynamic programming  
  - Cumulative optimization  
  - Edge case handling  

- **Solution File:**  
  `solution.py`

- **Reflection:**  
  This problem reinforced the power of **dynamic programming**. Kadane’s algorithm taught me how to optimize cumulative sums and handle negative values effectively.
