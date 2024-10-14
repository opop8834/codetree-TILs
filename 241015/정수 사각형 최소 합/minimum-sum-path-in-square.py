n = int(input())

dp = [[-1 for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]

for i in range(n):
    temp = input().split(" ")
    for j in range(n):
        if temp[j].strip() and temp[j].isdigit():
            graph[i].append(int(temp[j]))
            
if n == 1:
    print(graph[0][0])
else:
    
    dp[0][n-1] = graph[0][n-1]
    dp[0][n-2] = graph[0][n-1] + graph[0][n-2]
    dp[1][n-1] = graph[0][n-1] + graph[1][n-1]
    for i in range(n):
        for j in range(n-1,-1,-1):
            if i == 0 and j <= n-3:
                dp[i][j] = graph[i][j] + dp[i][j+1]
            elif j == n-1 and i >= 2:
                dp[i][j] = graph[i][j] + dp[i-1][j]
            elif i >=1 and j <= n-2:
                dp[i][j] = min(dp[i-1][j] + graph[i][j], dp[i][j+1] + graph[i][j])
    print(dp[n-1][0])