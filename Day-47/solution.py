
import numpy as np

class GradientDescentLinearRegression:
    def __init__(self, learning_rate=0.01, iterations=100):
        self.lr = learning_rate
        self.iterations = iterations
        self.m = 0  
        self.b = 0  
        self.loss_history = []

    def compute_loss(self, y_true, y_pred):
        """
        Mean Squared Error Loss
        """
        return np.mean((y_true - y_pred) ** 2)

    def fit(self, X, y):
        n = len(X)

        for i in range(self.iterations):
            y_pred = self.m * X + self.b

            dm = (-2/n) * np.sum(X * (y - y_pred))
            db = (-2/n) * np.sum(y - y_pred)

            self.m -= self.lr * dm
            self.b -= self.lr * db

            loss = self.compute_loss(y, y_pred)
            self.loss_history.append(loss)

            if i % 10 == 0:
                print(f"Iteration {i}: Loss = {loss:.4f}")

    def predict(self, X):
        return self.m * X + self.b


X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

model = GradientDescentLinearRegression(learning_rate=0.01, iterations=100)
model.fit(X, y)

predictions = model.predict(X)

print("\nFinal Parameters:")
print("Slope (m):", model.m)
print("Intercept (b):", model.b)
print("Predictions:", predictions)