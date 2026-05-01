## Day-52: Train/Test Split Manually (Model Logic - Vectors & Loss)

- **Problem Statement:**  
  Implement a manual train/test split function to divide datasets into training and testing sets.  
  This helps in understanding **model evaluation** and avoiding **data leakage**.

- **Challenge Overview:**  
  - This challenge focuses on dataset handling and validation basics.  
  - Instead of using libraries like `scikit-learn`, the split is done manually.  
  - Random shuffling ensures proper distribution of samples.  
  - The split ratio is controlled by the `test_size` parameter.  

- **Topics Covered:**  
  - Data splitting fundamentals  
  - Model validation basics  
  - Avoiding data leakage  
  - Random shuffling for unbiased distribution  
  - ML workflow essentials  

- **Solution File:**  
  `solution.py`  

- **Approach:**  
  - Convert input features and labels into numpy arrays.  
  - Shuffle indices to avoid ordered bias.  
  - Calculate split index based on `test_size`.  
  - Slice arrays into training and testing sets.  

- **Edge Cases Considered:**  
  - Small datasets (ensuring split still works).  
  - Reproducibility with `random_state`.  
  - Different test sizes (e.g., 20%, 30%).  

- **Reflection:**  
  This challenge strengthened my understanding of **data splitting and validation**.  
  I learned how manual splitting works behind the scenes of libraries like `scikit-learn`.  
  Practicing this gave me confidence in handling datasets carefully to avoid **data leakage** and ensure fair evaluation.  
  It also reinforced the importance of reproducibility in experiments by using random seeds.  
