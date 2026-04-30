## Day-51: Pandas (Vectors & Loss) – Clean Missing Values

- **Problem Statement:**  
  Handle missing values in datasets using Pandas to ensure clean and reliable data for machine learning and analysis.

- **Challenge Overview:**  
  - This challenge focuses on **data preprocessing** with Pandas.  
  - Missing values are common in real-world datasets and can negatively impact ML models.  
  - You will learn techniques to **detect, drop, or fill missing values**.  
  - Efficient handling of missing data improves the quality of predictions and reduces bias.  

- **Topics Covered:**  
  - Data cleaning techniques  
  - Handling missing values  
  - Pandas functions (`dropna`, `fillna`)  
  - Data preprocessing workflows  
  - Preparing datasets for ML  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  1. Create a sample dataset with missing values.  
  2. Use `dropna()` to remove rows containing missing values.  
  3. Use `fillna()` with column mean to replace missing numeric values.  
  4. Return both cleaned versions for comparison.  

- **Output:**  
  The program prints:  
  - Original DataFrame with missing values  
  - Cleaned DataFrame after dropping missing values  
  - Cleaned DataFrame after filling missing values with column means  

- **Reflection:**  
  This challenge helped me understand how **data preprocessing** is crucial before applying ML algorithms.  
  Handling missing values ensures that models are trained on consistent and reliable data.  
  Pandas provides simple yet powerful tools (`dropna`, `fillna`) to manage missing data efficiently.  
  Mastering these techniques strengthens confidence in preparing datasets for **machine learning workflows**.  
