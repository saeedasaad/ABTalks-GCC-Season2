def contains_duplicate_bruteforce(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def contains_duplicate_sorting(nums):
    nums.sort()  
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

def contains_duplicate_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],        
        [1, 2, 3, 4, 1],        
        [10, 20, 30, 40, 50],   
        [7, 7, 7, 7],           
    ]

    print("=== Contains Duplicate Challenge ===\n")
    for nums in test_cases:
        print(f"Input: {nums}")
        print(f"Brute Force: {contains_duplicate_bruteforce(nums)}")
        print(f"Sorting:     {contains_duplicate_sorting(nums[:])}") 
        print(f"HashSet:     {contains_duplicate_set(nums)}")
        print("-" * 40)