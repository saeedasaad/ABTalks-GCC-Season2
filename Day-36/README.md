## Day-36: Container With Most Water (Two Pointers - Optimization)

- **Problem Statement:**  
  Given an array `height` where each element represents the height of a vertical line, find two lines that together with the x-axis form a container such that the container holds the most water. Return the maximum amount of water it can store.

- **Challenge Overview:**  
  - The brute force approach checks all pairs, resulting in O(n²) complexity.  
  - The optimized solution uses the Two Pointers technique to reduce complexity to O(n).  
  - Start with pointers at both ends and calculate the area between them.  
  - Move the pointer pointing to the shorter line inward to potentially find a taller boundary.  
  - This greedy strategy works because the area is limited by the shorter height.  
  - This problem is a classic interview question focused on optimization and pointer strategies.  

- **Topics Covered:**  
  - Two Pointers technique  
  - Greedy optimization strategy  
  - Time complexity improvement from O(n²) to O(n)  
  - Array traversal and boundary logic  
  - Interview problem-solving patterns  

- **Solution File:**  
  `solution.py`  

- **Reflection:**  
  This problem strengthened my understanding of the Two Pointers technique and how it can drastically reduce time complexity. Instead of checking all combinations, intelligently moving pointers based on height allowed an efficient solution. It highlighted the importance of recognizing patterns where greedy decisions lead to optimal results. Practicing this problem improved my ability to think in terms of optimization and prepared me for similar high-frequency interview questions.