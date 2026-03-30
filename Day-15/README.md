### Day-15: Big-O in Python (Contains Duplicate)

- **Problem Statement:**  
  Given a list of integers, determine if the list contains any duplicates.  
  Return `True` if duplicates exist, otherwise `False`.  

- **Challenge Overview:**  
  - Work with a list of elements and analyze the presence of duplicate values.  
  - Understand how different approaches impact time complexity.  
  - Apply efficient logic to detect duplicates in the dataset.  
  - Compare approaches based on performance using Big-O analysis.  

- **Topics Covered:**  
  - Understanding Big-O notation  
  - Analyzing time and space complexity  
  - Optimizing code for better performance  
  - Working with lists and sets in Python  
  - Preparing for coding interviews  

- **Problems Solved:**  
  1. **Contains Duplicate – Brute Force**  
     - Checked for duplicates using nested loops.  
     - Demonstrated inefficiency of `O(n^2)` time complexity.  

  2. **Contains Duplicate – Sorting**  
     - Sorted the list and checked adjacent elements.  
     - Improved efficiency to `O(n log n)`, but sorting adds overhead.  

  3. **Contains Duplicate – HashSet (Optimal)**  
     - Used a set to track seen elements.  
     - Achieved optimal `O(n)` time complexity with `O(n)` space usage.  

- **Solution File:**  
  `Day-15/solution.py`

- **Complexity Comparison:**  

  | Approach        | Time Complexity | Space Complexity | Notes                        |
  |-----------------|-----------------|------------------|------------------------------|
  | Brute Force     | O(n^2)          | O(1)             | Too slow for large inputs    |
  | Sorting         | O(n log n)      | O(1)/O(n)        | Relies on sorting            |
  | HashSet         | O(n)            | O(n)             | Best balance of speed & space|

- **Reflection:**  
  This challenge highlighted the importance of **choosing the right algorithm**:  
  - Brute force solutions are simple but inefficient.  
  - Sorting introduces logarithmic complexity but is still suboptimal.  
  - HashSet provides the most efficient solution, balancing speed and space.  

  By analyzing Big-O notation, I strengthened my ability to evaluate trade-offs and write interview-ready solutions.  
  Consistency in solving and documenting challenges continues to build my confidence and inspire others in the community.


