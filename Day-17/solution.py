def climbStairs_recursive(n):
    if n <= 2:
        return n
    return climbStairs_recursive(n - 1) + climbStairs_recursive(n - 2)

def climbStairs_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = climbStairs_memo(n - 1, memo) + climbStairs_memo(n - 2, memo)
    return memo[n]

def climbStairs_dp(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == "__main__":
    n = 5
    print("Recursive:", climbStairs_recursive(n))
    print("Memoization:", climbStairs_memo(n))
    print("DP Tabulation:", climbStairs_dp(n))