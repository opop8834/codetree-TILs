from collections import deque

n,k = map(int, input().split(" "))

visited = [[False for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]

for i in range(n):
    temp = input().split(" ")
    for j in range(len(temp)):
        if temp[j].strip() and temp[j].isdigit():
            graph[i].append(int(temp[j]))
            
r,c = map(int,input().split(" "))
r -= 1
c -= 1

dx , dy = [1,0, -1, 0] ,[0,1, 0, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    old_x, old_y = x, y
    max_number = - 999
    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x , new_y = x + dx[i], y +dy[i]
            if new_x >=0 and new_x < n and new_y >= 0 and new_y < n and not visited[new_x][new_y] and graph[new_x][new_y] < graph[old_x][old_y]:
                if graph[new_x][new_y] > max_number:
                    max_number = graph[new_x][new_y]
                visited[new_x][new_y] = True 
                q.append((new_x,new_y))
    for i in range(n):
        for j in range(n):
            if graph[i][j] == max_number:
                return i,j
    return -1,-1

for i in range(k):
    new_r, new_c = bfs(r,c)
    if new_r == -1 and new_c == -1:
        break
    r = new_r
    c = new_c
    visited = [[False for _ in range(n)] for _ in range(n)]
print(r+1, c+1)