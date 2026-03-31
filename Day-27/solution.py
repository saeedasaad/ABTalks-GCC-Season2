def containsNearbyDuplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))  
print(containsNearbyDuplicate([1,0,1,1], 1))  
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))  