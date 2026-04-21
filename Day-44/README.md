## Day-44: House Robber (Dynamic Programming - 1-D DP)

- **Problem Statement:**  
  You are given an integer array `nums` representing the amount of money in each house.  
  Adjacent houses cannot be robbed on the same night due to security systems.  
  Return the maximum amount of money you can rob without alerting the police.

---

- **Challenge Overview:**  
  - This challenge introduces **Dynamic Programming (DP)** with a focus on **1-D DP optimization**.  
  - Instead of solving the problem recursively, we break it into smaller overlapping subproblems.  
  - At each house, we decide whether to **rob it or skip it** based on maximum profit.  
  - The solution is optimized to use **constant space O(1)** instead of an array.  

---

- **Topics Covered:**  
  - Dynamic Programming (DP)  
  - 1-D DP optimization  
  - State transition  
  - Space optimization  
  - Greedy decision making within DP  

---

- **Solution File:**  
  `solution.py`

---

- **Approach:**  
  - If we rob the current house, we cannot rob the previous one.  
  - If we skip the current house, we take the previous maximum.  
  - Recurrence relation:  

    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

  - Instead of storing full DP array, we use two variables:
    - `prev1` → max money till previous house  
    - `prev2` → max money till house before previous  

  - Iterate through the list and update values accordingly.

---

- **Edge Cases Considered:**  
  - Empty array  
  - Single house  
  - Two houses  
  - Large input sizes  
  - All values are zero  

---

- **Time Complexity:**  
  - O(n), where n is number of houses  

- **Space Complexity:**  
  - O(1), constant space  

---

- **Reflection:**  
  This problem is a classic example of **1-D Dynamic Programming**.  
  It highlights how problems with **overlapping subproblems** can be optimized using DP.  
  The key takeaway is recognizing the pattern of **choosing between two states**.  
  This pattern appears frequently in interview problems like:
  - House Robber II  
  - Maximum sum of non-adjacent elements  
  - Climbing stairs variations  

  Mastering this builds a strong foundation for advanced DP problems.