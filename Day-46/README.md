## Day-46: Linear Regression (AI / Machine Learning Basics)

- **Problem Statement:**  
  Implement Linear Regression using Python to understand how machines learn patterns from data and make predictions.

- **Challenge Overview:**  
  - This challenge introduces the basics of Artificial Intelligence (AI) and Machine Learning (ML).  
  - Linear Regression is a simple supervised learning algorithm used to model the relationship between input and output.  
  - The goal is to find the best-fit line using the equation `y = mx + b`.  
  - Instead of using libraries like scikit-learn, we implement it from scratch to understand the core logic.  

- **Topics Covered:**  
  - AI vs Machine Learning basics  
  - Supervised learning  
  - Linear regression fundamentals  
  - Mathematical modeling (slope and intercept)  
  - Prediction using trained model  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  - Calculate mean of input (X) and output (y)  
  - Compute slope (m) using the formula:  
    `m = Σ((X - mean(X)) * (y - mean(y))) / Σ((X - mean(X))^2)`  
  - Compute intercept (b):  
    `b = mean(y) - m * mean(X)`  
  - Use the equation `y = mx + b` to predict values  

- **Output:**  
  The model prints:  
  - Slope (m)  
  - Intercept (b)  
  - Predicted values based on input data  

- **Reflection:**  
  This challenge helped me understand how machine learning models learn from data using mathematical formulas. Implementing linear regression from scratch improved my understanding of supervised learning and prediction logic. It also gave me insight into how libraries like scikit-learn work internally.  