## Day-53: Feature Scaling Implementation (AI + DSA)

- **Problem Statement:**  
  Implement feature scaling techniques to normalize data for machine learning models.  
  Scaling ensures faster convergence and better performance in algorithms sensitive to feature magnitude.

- **Challenge Overview:**  
  - Focus on **feature logic** using vectors and loss.  
  - Implement **normalization (Min-Max scaling)** and **standardization (Z-score scaling)** manually.  
  - Strengthen ML preprocessing skills by coding transformations without external libraries.  

- **Topics Covered:**  
  - Feature scaling concepts  
  - Normalization (range [0,1])  
  - Standardization (mean=0, std=1)  
  - Mathematical understanding of data transformation  
  - Preparing data for ML algorithms  

- **Solution File:**  
  `solution.py`

- **Approach:**  
  - **Min-Max Scaling:**  
    

\[
    x' = \frac{x - \min(x)}{\max(x) - \min(x)}
    \]

  
    Rescales values between 0 and 1.  

  - **Standardization:**  
    

\[
    z = \frac{x - \mu}{\sigma}
    \]

  
    Centers data around mean 0 with unit variance.  

- **Example:**  
  Input: `[10, 20, 30, 40, 50]`  
  - Min-Max Scaling → `[0.0, 0.25, 0.5, 0.75, 1.0]`  
  - Standardization → `[-1.414, -0.707, 0.0, 0.707, 1.414]`  

- **Edge Cases Considered:**  
  - Single-value dataset → scaling returns `[0]` or `[NaN]` depending on method.  
  - Negative values → handled correctly.  
  - Large ranges → normalized to [0,1].  

- **Reflection:**  
  This challenge reinforced the importance of **data preprocessing** in ML workflows.  
  I learned how scaling impacts convergence in gradient descent and improves model reliability.  
  Implementing these transformations manually deepened my mathematical intuition behind ML preprocessing.
