## Day-47: Gradient Descent (AI Math - Vectors & Loss)

- **Problem Statement:**  
  Implement Gradient Descent manually in Python to understand how machine learning models minimize error using iterative optimization.

- **Challenge Overview:**  
  - This challenge focuses on the mathematical foundation of AI, including vectors, loss functions, and optimization.  
  - Gradient Descent is used to minimize the loss function by updating model parameters step-by-step.  
  - We apply it to Linear Regression to find optimal values of slope (m) and intercept (b).  
  - The model learns by reducing error over multiple iterations.  

- **Topics Covered:**  
  - Vectors and basic linear algebra  
  - Loss functions (Mean Squared Error)  
  - Gradient Descent optimization  
  - Parameter updates (weights & bias)  
  - Iterative learning process  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  - Initialize parameters (m and b)  
  - Use prediction formula: `y = mx + b`  
  - Compute loss using Mean Squared Error (MSE)  
  - Calculate gradients (dm, db)  
  - Update parameters using learning rate  
  - Repeat for multiple iterations to minimize loss  

- **Output:**  
  - Loss value decreases over iterations  
  - Final optimized values of m and b  
  - Predicted values based on trained model  

- **Reflection:**  
  This challenge helped me understand the core mathematical concept behind machine learning models. By manually implementing gradient descent, I learned how models improve over time by minimizing loss. It strengthened my understanding of optimization, vectors, and iterative learning, which are fundamental concepts in AI and ML.