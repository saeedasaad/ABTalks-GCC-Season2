
def isBadVersion(version: int) -> bool:
    return version >= bad_version  

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    solution = Solution()

    num1 = 4
    bad_version = num1
    print("First bad version (should be 4):", solution.firstBadVersion(10))

    num2 = 1
    bad_version = num2
    print("First bad version (should be 1):", solution.firstBadVersion(5))

    num3 = 7
    bad_version = num3
    print("First bad version (should be 7):", solution.firstBadVersion(10))