try:

    nums = list(map(int, input("Enter numbers separated by commas: ").split(",")))

    running_sum = []
    total = 0

    for num in nums:
        total += num        
        running_sum.append(total)  

    print(f"Running Sum: {running_sum}")

except ValueError:
    print("Invalid input! Please enter integers only.")