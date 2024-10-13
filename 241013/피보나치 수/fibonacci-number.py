n = int(input())
dp = [-1] * n
dp[0] = 1
dp[1] = 1
if n <= 1:
    print(1)
else:
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[-1])