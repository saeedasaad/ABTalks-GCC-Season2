class FeatureScaler:
    def __init__(self, data):
        self.data = data
    
    def min_max_scaling(self):
        """Normalize features to range [0,1]"""
        min_val = min(self.data)
        max_val = max(self.data)
        return [(x - min_val) / (max_val - min_val) for x in self.data]
    
    def standardization(self):
        """Standardize features to mean=0, std=1"""
        mean_val = sum(self.data) / len(self.data)
        variance = sum((x - mean_val) ** 2 for x in self.data) / len(self.data)
        std_dev = variance ** 0.5
        return [(x - mean_val) / std_dev for x in self.data]


if __name__ == "__main__":
    features = [10, 20, 30, 40, 50]

    scaler = FeatureScaler(features)

    print("Original Data:", features)
    print("Min-Max Scaling:", scaler.min_max_scaling())
    print("Standardization:", scaler.standardization())
