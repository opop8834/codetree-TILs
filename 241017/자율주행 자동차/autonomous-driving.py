from collections import deque
n,m = map(int, input().split())
x,y,d = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    temp = input().split()
    for j in range(m):
        graph[i].append(int(temp[j]))

dx,dy = [0,0,-1,1],[-1,1,0,0]  # 좌 우 상 하

def bfs(x,y, d):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    count = 0
    answer = 1
    while q:
        x,y = q.pop()
        if d == 0:  # 북이면 좌
            new_x, new_y = x + dx[0], y + dy[0]
        elif d == 1:  # 동이면 상
            new_x, new_y = x + dx[2], y + dy[2]
        elif d == 2:  # 남이면 우
            new_x, new_y = x + dx[1], y + dy[1]
        elif d == 3:  # 서이면 하
            new_x, new_y = x + dx[3], y + dy[3]
        
        if count >= 4:
            count = 0
            if d == 0:  # 북이면 하
                new_x, new_y = x + dx[3], y + dy[3]
            elif d == 1:  # 동이면 좌
                new_x, new_y = x + dx[0], y + dy[0]
            elif d == 2:  # 남이면 상
                new_x, new_y = x + dx[2], y + dy[2]
            elif d == 3:  # 서이면 우
                new_x, new_y = x + dx[1], y + dy[1]

            if new_x >= 0 and new_x < n and new_y >=0 and new_y < m and graph[new_x][new_y] == 1:
                break
            elif new_x >= 0 and new_x < n and new_y >=0 and new_y < m and visited[new_x][new_y] and graph[new_x][new_y] == 0:
                q.append((new_x,new_y))
                d += 1
                count = 0
        elif new_x >= 0 and new_x < n and new_y >=0 and new_y < m and not visited[new_x][new_y] and graph[new_x][new_y] == 0:
            count = 0
            visited[new_x][new_y] = True
            answer += 1
            q.append((new_x,new_y))
        elif new_x >= 0 and new_x < n and new_y >=0 and new_y < m and visited[new_x][new_y] and graph[new_x][new_y] == 0:
            q.append((x,y))
            count += 1
        elif new_x >= 0 and new_x < n and new_y >=0 and new_y < m and graph[new_x][new_y] == 1:
            q.append((x,y))
            count += 1
        if d <= 0:
            d = 3
        else:
            d -= 1
    print(answer)

bfs(x,y,d)