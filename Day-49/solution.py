import math
from collections import defaultdict

class SpamClassifier:
    def __init__(self):
        self.vocab = {}
        self.weights = defaultdict(float)
        self.bias = 0.0

    def tokenize(self, text):
        return text.lower().split()

    def build_vocab(self, messages):
        idx = 0
        for msg in messages:
            for word in self.tokenize(msg):
                if word not in self.vocab:
                    self.vocab[word] = idx
                    idx += 1

    def vectorize(self, text):
        vector = [0] * len(self.vocab)
        for word in self.tokenize(text):
            if word in self.vocab:
                vector[self.vocab[word]] += 1
        return vector

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def predict_proba(self, vector):
        z = self.bias
        for word, idx in self.vocab.items():
            z += self.weights[word] * vector[idx]
        return self.sigmoid(z)

    def predict(self, text):
        vector = self.vectorize(text)
        prob = self.predict_proba(vector)
        return 1 if prob >= 0.5 else 0

    def train(self, messages, labels, lr=0.1, epochs=100):
        self.build_vocab(messages)

        for _ in range(epochs):
            for msg, label in zip(messages, labels):
                vector = self.vectorize(msg)
                pred = self.predict_proba(vector)
                error = pred - label


                for word, idx in self.vocab.items():
                    self.weights[word] -= lr * error * vector[idx]


                self.bias -= lr * error

    def evaluate(self, messages, labels):
        correct = 0
        for msg, label in zip(messages, labels):
            if self.predict(msg) == label:
                correct += 1
        return correct / len(labels)


if __name__ == "__main__":
    messages = [
        "Win money now",
        "Limited offer claim prize",
        "Hello friend how are you",
        "Let's meet tomorrow",
        "Claim your free reward now",
        "Hi, are we still meeting?"
    ]

    labels = [1, 1, 0, 0, 1, 0]  

    model = SpamClassifier()
    model.train(messages, labels)

    test_msgs = [
        "Win a free prize now",
        "Hello, how are you?",
        "Claim your reward",
        "Are we meeting tomorrow?"
    ]

    print("Predictions:")
    for msg in test_msgs:
        print(f"{msg} -> {'Spam' if model.predict(msg) else 'Ham'}")

    accuracy = model.evaluate(messages, labels)
    print(f"\nTraining Accuracy: {accuracy:.2f}")