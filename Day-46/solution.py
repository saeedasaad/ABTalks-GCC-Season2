import numpy as np

class LinearRegression:
    def __init__(self):
        self.m = 0  
        self.b = 0  

    def fit(self, X, y):
        """
        Train the model using simple linear regression formula
        """
        n = len(X)

        # Mean values
        x_mean = np.mean(X)
        y_mean = np.mean(y)

        numerator = np.sum((X - x_mean) * (y - y_mean))
        denominator = np.sum((X - x_mean) ** 2)

        self.m = numerator / denominator

        self.b = y_mean - (self.m * x_mean)

    def predict(self, X):
        """
        Make predictions using y = mx + b
        """
        return self.m * X + self.b


X = np.array([1, 2, 3, 4, 5])   # Input feature
y = np.array([2, 4, 5, 4, 5])   # Output labels

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)

print("Slope (m):", model.m)
print("Intercept (b):", model.b)
print("Predictions:", predictions)