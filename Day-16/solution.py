
def fibonacci(n):
    """
    Recursive function to find nth Fibonacci number
    """
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")