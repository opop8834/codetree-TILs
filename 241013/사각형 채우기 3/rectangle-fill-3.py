n = int(input())
dp = [-1]* (n+1)

dp[0] = 0
dp[1] = 2

for i in range(2, n+1):
    dp[i] = dp[i-1] * 3 + 1
print(dp[-1]% 1000000007)