def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left)
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11, 13,5,19,14,7.5,7,26,9,2,5,7]
    target = 7
    result = binary_search_iterative(nums, target)
    print(f"Target {target} found at index: {result}")