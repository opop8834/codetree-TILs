from collections import deque
import itertools
import copy

n,k,m = map(int, input().split(" "))

visited = [[False for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]


for i in range(n):
    temp = input().split(" ")
    for j in range(len(temp)):
        if temp[j].strip() and temp[j].isdigit():
            graph[i].append(int(temp[j]))


dx, dy = [0,0,-1,1],[-1,1,0,0]
count = 0

def bfs(x,y, graph):
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    global count
    count += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x >=0 and new_x < n and new_y >=0 and new_y < n and not visited[new_x][new_y] and graph[new_x][new_y] == 0:
                count += 1
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
            # 1인구간인 돌들을 m개 만큼 치우기

com_ = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            com_.append((i,j))
combinations = list(itertools.combinations(com_, m))

max_count = -999
for i in range(k):
    r,c = map(int, input().split(" "))
    r -= 1
    c -= 1
    
    for com in combinations:
        new_graph = copy.deepcopy(graph)
        for x,y in com:
            new_graph[x][y] = 0
        bfs(r,c,new_graph)
        if count > max_count:
            max_count = count
        count = 0
        visited = [[False for _ in range(n)] for _ in range(n)]
print(max_count)