n = int(input())
dp = [-1] * (n+1)

if n == 1:
    print(1)
elif n == 2 :
    print(2)
else:
    dp[1] = 1
    dp[2] = 2
    # dp[3] = 3
    # dp[4] = 5
    # dp[5] = 8

    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    print(dp[-1])