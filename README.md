# ABTalks GCC Season-2 

This repository contains my solutions for the **Global Coding Challenge (Season-2)** organized by ABTalksOnAI.  
I am documenting my progress day by day to build consistency, confidence, and share my learning journey publicly.

---

##  Repository Structure

```
ABTalks-GCC-Season2/ 
│ ├── Day-01/ 
│   └── solution.py 
│ ├── Day-02/ 
│   └── solution.py 
│ ├── Day-03/
│   └── solution.py
│ ├── Day-04/
│   └── solution.py
│ ├── Day-05/
│   └── solution.
│ ├── Day-06/
│   └── solution.py
│ ├── Day-07/
│   └── solution.py
│ ├── Day-08/
│   └── solution.py
│ ├── Day-09/
│   └── solution.py
│ ├── Day-10/
│   └── solution.py
│ ├── Day-11/
│   └── solution.py
│ ├── Day-12/
│   └── solution.py
│ ├── Day-13/
│   └── solution.py
│ └── README.md
```
---

## Daily Challenges

### Day-01: Two Sum (Python Basics - Input/Output)
- **Problem Statement:**  
  Given an integer array `nums` and an integer `target`, find two distinct indices such that the numbers at those indices add up to the target.  
  Assumptions:  
  1. Exactly one valid solution exists.  
  2. You may not use the same element twice.  

- **Topics Covered:**  
  - Input / Output in Python  
  - List handling  
  - Loops and conditions  
  - Error handling  

- **Solution File:**  
  `Day-01/solution.py`

- **Reflection:**  
  Learned how to take user input, convert it into a list of integers, and apply logic to find pairs efficiently. Practiced error handling to make the program beginner-friendly and robust.

---

### Day-02: Running Sum of 1D Array (Python Basics - Variables & Data Types)
- **Problem Statement:**  
  Given a one-dimensional array of integers, compute the running sum of the array.  
  Rules:  
  - The first element remains the same.  
  - Each subsequent element becomes the sum of itself and all previous elements.  

- **Topics Covered:**  
  - Variables and data types  
  - List manipulation  
  - Looping concepts  
  - Logical thinking  

- **Solution File:**  
  `Day-02/solution.py`

- **Reflection:**  
  Practiced using variables and loops to build cumulative sums step by step. Strengthened understanding of how data types and list operations work together in Python.

---

### Day-03: Palindrome Number (Software Engineering - Control Flow)  
- **Problem Statement:**  
  Analyze a given number and determine whether it is a palindrome using control flow (`if-else`).  

- **Challenge Overview:**  
  - Analyze a given number.  
  - Determine whether the number is a palindrome.  
  - Use logical conditions to check the palindrome property.  
  - Display the result clearly.  

- **Topics Covered:**  
  - Control flow with if-else statements  
  - Conditional logic  
  - Working with numbers in Python  
  - Logical thinking and structured problem solving  
  - Writing clean and readable Python code  

- **Solution File:**  
  `Day-03/solution.py`  

- **Reflection:**  
  Practiced applying control flow to solve logical problems. Strengthened ability to structure conditions clearly and write beginner-friendly, readable code.  

---

### Day-04: Fizz Buzz (Software Engineering - Loops)

- **Problem Statement:**  
  Write a program that prints numbers from `1` to `n`.  
  However, follow these rules:

  - If a number is divisible by **3**, print `"Fizz"` instead of the number.
  - If a number is divisible by **5**, print `"Buzz"` instead of the number.
  - If a number is divisible by **both 3 and 5**, print `"FizzBuzz"`.
  - Otherwise, print the number itself.

- **Challenge Overview:**  
  - Iterate through a sequence of numbers.
  - Apply conditional logic to each number.
  - Print appropriate output based on the defined rules.

- **Topics Covered:**  
  - Loops (`for` / `while`)
  - Conditional statements
  - Modulus operator (`%`)
  - Logical problem solving
  - Writing clean and readable Python code

- **Solution File:**  
  `Day-04/solution.py`

- **Reflection:**  
  Practiced using loops to iterate through numbers and apply multiple conditions.  
  Learned how to combine iteration with logical checks using the modulus operator to implement the classic **Fizz Buzz** pattern, a common beginner and interview coding problem.

---

### Day-05: Number of Steps to Reduce a Number to Zero (Software Engineering - Loops & Logic Building)

- **Problem Statement:**  
  Accept a positive integer as input and apply specific rules to reduce the number step by step until it reaches zero.  
  Rules:  
  - If the number is even, divide it by 2.  
  - If the number is odd, subtract 1.  
  - Count and display the total number of steps taken.

- **Challenge Overview:**  
  - Accept user input.  
  - Apply loop-based iteration with conditional logic.  
  - Track the number of steps required to reach zero.  
  - Display the result clearly.  

- **Topics Covered:**  
  - Loop-based iteration (`while` loop)  
  - Conditional statements (`if-else`)  
  - Logical problem-solving techniques  
  - Writing efficient Python code  
  - Algorithmic thinking used in coding interviews  

- **Solution File:**  
  `Day-05/solution.py`

- **Reflection:**  
  Practiced combining loops with conditional logic to solve a structured problem.  
  Strengthened ability to design efficient algorithms and write clean, beginner-friendly Python code.  
  Learned how to break down a problem into smaller steps and apply logical thinking to reach the solution.

  ---
### Day-06: Power of Two (Software Engineering - Functions & Return)

- **Problem Statement:**  
  Accept a number as input and use a function to determine whether the number is a power of two.  
  Rules:  
  - A number is a power of two if it can be expressed as \(2^n\) (where \(n\) is a non-negative integer).  
  - Return the result from the function and display it clearly.

- **Challenge Overview:**  
  - Accept user input.  
  - Use a function to encapsulate the logic.  
  - Apply conditional checks to verify the power of two property.  
  - Return `True` or `False` from the function.  
  - Display the result clearly to the user.  

- **Topics Covered:**  
  - Creating and calling Python functions  
  - Using return statements effectively  
  - Applying logical reasoning in programming  
  - Writing modular and reusable code  
  - Strengthening algorithmic thinking  

- **Solution File:**  
  `Day-06/solution.py`

- **Reflection:**  
  Practiced writing modular functions with clear responsibilities.  
  Strengthened understanding of how return statements work in Python.  
  Learned how to apply logical reasoning to check mathematical properties.  
  Built confidence in writing clean, reusable, and beginner-friendly code.

  ---
### Day-07: Best Time to Buy and Sell Stock (Software Engineering - Python Mini Practice)

- **Problem Statement:**  
  Given a list of stock prices where each element represents the price of a stock on a given day, determine the maximum profit you can achieve by choosing a single day to buy and a different day in the future to sell.  
  Assumptions:  
  1. You must buy before you sell.  
  2. If no profit can be made, return 0.  

- **Challenge Overview:**  
  - Work with a list representing stock prices over a period of time.  
  - Analyze the sequence of prices to determine the best opportunity for buying and selling.  
  - Apply logical reasoning and efficient problem-solving strategies.  
  - Implement your approach using Python and display the result clearly.  

- **Topics Covered:**  
  - Logical thinking and algorithmic reasoning  
  - Working with Python lists and numerical data  
  - Problem-solving using efficient approaches  
  - Writing clean and structured Python code  
  - Understanding common technical interview problems  

- **Solution File:**  
  `Day-07/solution.py`

- **Reflection:**  
  Practiced analyzing numerical patterns to make optimal decisions. Strengthened ability to design efficient algorithms by tracking minimum prices and maximum profits dynamically. Learned how to approach a classic interview problem with clarity, efficiency, and clean Python code.
  
  ---
  ### Day-08: Find Numbers with Even Number of Digits (Software Engineering - Lists & Traversal)

- **Problem Statement:**  
  Given a list of integers, determine how many numbers contain an even number of digits.  

- **Challenge Overview:**  
  - Work with a list containing multiple integer values.  
  - Traverse through each element of the list.  
  - Analyze each number based on its digit length.  
  - Identify numbers that satisfy the required condition.  
  - Display the final count clearly.  

- **Topics Covered:**  
  - Working with Python lists  
  - Traversing data structures efficiently  
  - Applying logical conditions during iteration  
  - Writing clean and structured Python code  
  - Strengthening algorithmic problem-solving skills  

- **Solution File:**  
  `Day-08/solution.py`

- **Reflection:**  
  Practiced list traversal and applied logical conditions to analyze digit lengths. Strengthened ability to work with Python lists and write clean, beginner-friendly code. Learned how to break down problems into smaller steps and apply efficient iteration techniques.

  ---
  ### Day-09: Maximum Subarray (Software Engineering - Kadane’s Algorithm)

- **Problem Statement:**  
  Given a list of integers (both positive and negative), find the contiguous subarray with the maximum sum using Kadane’s Algorithm.  

- **Challenge Overview:**  
  - Work with a list containing positive and negative integers.  
  - Traverse through the list to evaluate possible subarrays.  
  - Apply Kadane’s Algorithm to determine the maximum sum efficiently.  
  - Display the final maximum subarray sum clearly.  

- **Topics Covered:**  
  - Working with Python lists  
  - Understanding Kadane’s Algorithm  
  - Efficient traversal and dynamic decision making  
  - Writing optimized and structured Python code  
  - Strengthening algorithmic and interview problem-solving skills  

- **Solution File:**  
  `Day-09/solution.py`

- **Reflection:**  
  Learned how to apply Kadane’s Algorithm to solve a classic interview problem. Practiced efficient traversal and dynamic decision making. Strengthened ability to write optimized code and gained confidence in solving problems involving subarrays and numerical analysis.

  ---

  ### Day-10: Move Zeroes (Software Engineering - Lists & Rearrangement)

- **Problem Statement:**  
  Given a list of integers, rearrange the elements so that all zero values are moved to the end of the list while maintaining the relative order of the non-zero elements.

- **Challenge Overview:**  
  - Work with a list containing integers including zero values.  
  - Apply logical operations to rearrange elements within the list.  
  - Ensure that all zero values are moved to the end of the list.  
  - Maintain the relative order of the non-zero elements during the rearrangement.  

- **Topics Covered:**  
  - Working with lists and array manipulation  
  - Logical thinking for element rearrangement  
  - Efficient traversal of data structures  
  - Writing clean and structured Python code  
  - Preparing for common coding interview problems  

- **Solution File:**  
  `Day-10/solution.py`

- **Reflection:**  
  Practiced list manipulation and rearrangement techniques by solving the classic **Move Zeroes** problem. Learned how to preserve the order of non-zero elements while efficiently moving zeroes to the end. Strengthened understanding of list comprehension, counting, and concatenation in Python. This challenge reinforced confidence in solving interview-style problems and writing clean, beginner-friendly code.

  
  ---

  ### Day-11: Reverse String (Software Engineering - Strings & Slicing)

- **Problem Statement:**  
  Given a string input, reverse the string and display the result.  

- **Challenge Overview:**  
  - Work with a given string input.  
  - Apply logical operations to reverse the string.  
  - Explore Python string techniques such as slicing or traversal.  
  - Display the reversed string as the final output.  

- **Topics Covered:**  
  - Working with strings in Python  
  - Understanding string slicing concepts  
  - Applying logical thinking for string manipulation  
  - Writing clean and structured Python code  
  - Building confidence for coding interview questions  

- **Solution File:**  
  `Day-11/solution.py`

- **Reflection:**  
  Practiced string manipulation using Python’s slicing technique. Learned how to reverse a string in a clean and efficient way. Strengthened understanding of how slicing works with step values, and gained confidence in solving interview-style problems involving strings. This challenge reinforced the importance of mastering fundamental operations like slicing and traversal for real-world development.

  ---

  ### Day-12: Valid Anagram (Software Engineering - Strings & Frequency)

- **Problem Statement:**  
  Given two strings, determine whether they are valid anagrams of each other.  
  An anagram is formed when two strings contain the same characters with the same frequency, but possibly in a different order.

- **Challenge Overview:**  
  - Work with two strings as input.  
  - Analyze the frequency of characters within each string.  
  - Compare the character distributions between both strings.  
  - Determine whether the strings satisfy the required condition for an anagram.  

- **Topics Covered:**  
  - Working with strings and character operations  
  - Frequency analysis in programming  
  - Logical comparison of string structures  
  - Writing clean and structured Python code  
  - Strengthening problem-solving skills for coding interviews  

- **Solution File:**  
  `Day-12/solution.py`

- **Reflection:**  
  Practiced analyzing character frequencies to solve the classic **Valid Anagram** problem. Learned how to use dictionaries to count occurrences of characters and compare distributions between two strings. Strengthened logical thinking and problem-solving skills by applying frequency analysis. This challenge reinforced confidence in handling string operations and prepared me for interview-style questions involving string manipulation.

---

  ### Day-13: Length of Last Word (Software Engineering - Strings & Parsing)

- **Problem Statement:**  
  Given a string that may contain multiple words separated by spaces, determine the **length of the last word** in the string.
  A **word** is defined as a sequence of **non-space characters**.
  The goal is to correctly parse the string, handle extra spaces, and return the length of the final word.


- **Challenge Overview:**  
  - Work with a string input that may contain multiple words.
  - Parse and analyze the text to identify the **last word**.
  - Handle **edge cases** such as trailing spaces.
  - Return the **length of the last word** clearly.


- **Topics Covered:**  
  - Working with **strings in Python**
  - **String parsing techniques** (`strip()`, `split()`)
  - Efficient **text processing**
  - Writing **clean and structured Python code**
  - Practicing **interview-style string manipulation problems**


- **Solution File:**  
  `Day-12/solution.py`