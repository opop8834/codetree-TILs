n = int(input())
dp = [-1] * (n+1)
# dp[4] = 1  dp[2] + dp[2]
# dp[5] = 2  dp[3] + dp[2]
# dp[6] = 2  dp[3] + dp[3]  or dp[2] dp[2] dp[2]
# dp[7] = 3  dp[3] + dp[3] + dp[2]

# 2나 3으로 나눌때 0이 되면 1
if n <=1:
    print(0)
elif n <=3:
    print(1)
else:
    dp[0] = 0
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        # count = 0
        # if i % 2 == 0:
        #     count += 1
        # if i % 3 == 0:
        #     count += 1
        
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[-1] % 10007)