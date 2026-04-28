## Day-49: Spam Classifier (Machine Learning - Classification, Vectors & Loss)

- **Problem Statement:**  
  Design the logic of a spam classifier that categorizes messages (emails/SMS) as **Spam** or **Not Spam (Ham)**.  
  Implement feature extraction, vector representation, and a simple classification model using Python.

---

- **Challenge Overview:**  
  - This challenge introduces **Binary Classification** using core ML concepts.  
  - Text data is converted into numerical vectors through **feature engineering**.  
  - A **logistic regression-style model** is used to compute probabilities.  
  - A **loss function (log loss)** helps evaluate prediction performance.

---

- **Topics Covered:**  
  - Binary Classification  
  - Feature Engineering (Bag of Words)  
  - Vectorization  
  - Sigmoid Function  
  - Log Loss  
  - Model Evaluation (Accuracy)  

---

- **Solution File:**  
  `solution.py`

---

- **Approach:**  
  - Convert messages into **Bag-of-Words vectors**.  
  - Assign weights to each word in the vocabulary.  
  - Compute linear combination:  

    z = w·x + b  

  - Apply sigmoid function:  

    p = 1 / (1 + e^-z)  

  - Classification rule:  
    - If p ≥ 0.5 → Spam  
    - Else → Ham  

  - Optimize weights using **Gradient Descent** to minimize log loss.

---

- **Edge Cases Considered:**  
  - Empty message  
  - Unknown or unseen words  
  - All labels belong to one class  
  - Very short messages  
  - Repeated words  

---

- **Time Complexity:**  
  - O(n × m), where n = number of messages and m = average words per message  

- **Space Complexity:**  
  - O(v), where v = vocabulary size  

---

- **Reflection:**  
  This problem builds a strong foundation for **text classification systems**.  
  It demonstrates how raw text can be transformed into vectors and used in a mathematical model for prediction.  
  The concepts learned here extend to:  
  - Naive Bayes  
  - TF-IDF vectorization  
  - Deep Learning models (RNNs, Transformers)  
