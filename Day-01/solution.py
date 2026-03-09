try:
    nums = list(map(int, input("Enter numbers separated by commas: ").split(",")))
    target = int(input("Enter target value: "))

    found = False
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Indices: [{i}, {j}]")
                found = True
                break
        if found:
            break

    if not found:
        print("No valid pair found.")
except ValueError:
    print("Invalid input! Please enter integers only.")