import numpy as np

class SimpleLinearRegression:
    def __init__(self):
        self.m = 0 
        self.b = 0 

    def fit(self, X, y):
        """
        Train model using closed-form linear regression
        """
        x_mean = np.mean(X)
        y_mean = np.mean(y)

        numerator = np.sum((X - x_mean) * (y - y_mean))
        denominator = np.sum((X - x_mean) ** 2)

        self.m = numerator / denominator
        self.b = y_mean - (self.m * x_mean)

    def predict(self, X):
        return self.m * X + self.b

X = np.array([500, 800, 1000, 1200, 1500])  
y = np.array([150, 200, 250, 300, 360])     


model = SimpleLinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("Slope (m):", model.m)
print("Intercept (b):", model.b)
print("Predictions:", predictions)


new_size = np.array([1100])
predicted_price = model.predict(new_size)
print("Predicted price for 1100 sq.ft house:", predicted_price)