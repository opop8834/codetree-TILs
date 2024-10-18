from collections import deque

n, L, R = map(int, input().split())

visited = [[False for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]
break_time = 0
for i in range(n):
    temp = input().split()
    for j in range(n):
        graph[i].append(int(temp[j]))


dx, dy = [0,0,-1,1], [-1,1,0,0]
def bfs(x,y):
    global break_time
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    count = 1
    sum_ = graph[x][y]
    change = []
    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x , new_y = x + dx[i], y + dy[i]
            if new_x >=0 and new_x < n and new_y >=0 and new_y < n :
                if abs(graph[new_x][new_y] - graph[x][y]) >= L and abs(graph[new_x][new_y] - graph[x][y]) <= R and not visited[new_x][new_y]:
                    change.append((x,y))
                    change.append((new_x,new_y))
                    count += 1
                    sum_ += graph[new_x][new_y]
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
    if count != 1:
        break_time += 1
        change_result = set(change)
        for s in change_result:
            graph[s[0]][s[1]] = int(sum_ / count)
answer = 0
while(True):
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j)
    if break_time == 0:
        break
    break_time = 0
    answer += 1
    visited = [[False for _ in range(n)] for _ in range(n)]
print(answer)