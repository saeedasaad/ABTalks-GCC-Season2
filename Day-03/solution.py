try:

    num = int(input("Enter a number: "))

    num_str = str(num)

    if num_str == num_str[::-1]:
        print(f"{num} is a Palindrome Number.")
    else:
        print(f"{num} is NOT a Palindrome Number.")

except ValueError:
    print("Invalid input! Please enter a valid integer.")