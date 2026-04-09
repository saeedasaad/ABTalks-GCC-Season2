## Day-35: Longest Substring Without Repeating Characters (Sliding Window - Variable Window)

- **Problem Statement:**  
  Given a string `s`, find the length of the longest substring without repeating characters.  

- **Challenge Overview:**  
  - This problem is a classic example of the **variable sliding window technique**.  
  - A brute-force approach would check all substrings, leading to `O(n^2)` complexity.  
  - The optimal solution uses a **dynamic window** with two pointers (`left`, `right`) and a set to track characters.  
  - When a duplicate character is found, the window shrinks from the left until the constraint is satisfied.  
  - This ensures an efficient **O(n)** time complexity since each character is processed at most twice.  

- **Topics Covered:**  
  - Sliding window (variable size)  
  - Two-pointer technique  
  - Hash set for fast lookup  
  - String processing  
  - Time complexity optimization (O(n))  

- **Solution File:**  
  `solution.py`  

- **Reflection:**  
  This challenge strengthened my understanding of **dynamic window resizing** in sliding window problems.  
  Instead of restarting the search on duplicates, I learned how to efficiently adjust the window to maintain valid constraints.  
  The use of a set ensured constant-time lookups, making the solution optimal.  

  This pattern is widely used in real-world scenarios like **data stream processing, substring search, and log analysis**, where performance matters.  
  Practicing this problem improved my ability to handle **variable constraints dynamically**, which is a key skill for technical interviews and scalable system design.