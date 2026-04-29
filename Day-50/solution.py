import numpy as np

def calculate_mean_variance(arr):
    """
    Function to calculate mean and variance using NumPy.
    
    Parameters:
    arr (list or numpy.ndarray): Input array of numbers
    
    Returns:
    tuple: mean, variance
    """
    np_array = np.array(arr)
    mean_val = np.mean(np_array)
    variance_val = np.var(np_array)
    return mean_val, variance_val


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    mean, variance = calculate_mean_variance(data)
    print("Data:", data)
    print("Mean:", mean)
    print("Variance:", variance)
