def count_even_digit_numbers(nums):
    count = 0
    for num in nums:

        if len(str(num)) % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":

    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    result = count_even_digit_numbers(nums)
    print("Count of numbers with even digits:", result)