import numpy as np

def train_test_split_manual(X, y, test_size=0.2, random_state=None):

    if random_state is not None:
        np.random.seed(random_state)

    X = np.array(X)
    y = np.array(y)

    indices = np.arange(len(X))
    np.random.shuffle(indices)

    split_idx = int(len(X) * (1 - test_size))
    
    train_idx, test_idx = indices[:split_idx], indices[split_idx:]
    
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


if __name__ == "__main__":
    X = [[i] for i in range(10)]  
    y = [i % 2 for i in range(10)]  
    
    X_train, X_test, y_train, y_test = train_test_split_manual(X, y, test_size=0.3, random_state=42)
    
    print("Training Features:", X_train)
    print("Testing Features:", X_test)
    print("Training Labels:", y_train)
    print("Testing Labels:", y_test)
