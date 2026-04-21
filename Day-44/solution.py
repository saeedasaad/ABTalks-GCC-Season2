def rob(nums):

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    prev2 = 0          
    prev1 = nums[0]    


    for i in range(1, len(nums)):

        current = max(prev1, prev2 + nums[i])

        prev2 = prev1
        prev1 = current

    return prev1


if __name__ == "__main__":
    houses = [2, 7, 9, 3, 1]
    print("Maximum amount that can be robbed:", rob(houses))