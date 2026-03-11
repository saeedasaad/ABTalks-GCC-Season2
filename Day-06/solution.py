def is_power_of_two(num):
    if num <= 0:
        return False

    while num % 2 == 0:
        num = num // 2

    return num == 1

user_input = int(input("Enter a number: "))
if is_power_of_two(user_input):
    print(f"{user_input} is a power of two.")
else:
    print(f"{user_input} is NOT a power of two.")