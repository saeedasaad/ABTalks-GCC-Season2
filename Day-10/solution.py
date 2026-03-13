def move_zeroes(nums):

    non_zero = [x for x in nums if x != 0]

    zero_count = len(nums) - len(non_zero)
    
    result = non_zero + [0] * zero_count
    
    return result


# nums = [0, 1, 0, 3, 12]
nums = [10,20,30,40,50]
print("Original List:", nums)
print("After Rearrangement:", move_zeroes(nums))