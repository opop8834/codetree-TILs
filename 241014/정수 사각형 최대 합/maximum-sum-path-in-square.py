n = int(input())

dp = [[-1 for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]

for i in range(n):
    temp = input().split(" ")
    for j in range(n):
        if temp[j].strip() and temp[j].isdigit():
            graph[i].append(int(temp[j]))

if n == 1:
    print(1)
else:
    dp[0][0] = graph[0][0]
    dp[0][1] = graph[0][1] + graph[0][0]
    dp[1][0] = graph[1][0] + graph[0][0]
    for i in range(n):
        for j in range(n):
            if i == 0 and j >=2:
                dp[i][j] = graph[i][j] + dp[i][j-1]
            elif j == 0 and i >= 2:
                dp[i][j] = graph[i][j] + dp[i-1][j]
            elif i >=1 and j>=1:
                dp[i][j] = max(graph[i][j] + dp[i][j-1], graph[i][j] + dp[i-1][j])
    # print(dp)
    print(dp[-1][-1])