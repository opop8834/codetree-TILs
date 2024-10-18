from collections import deque
import itertools
import sys

n,m = map(int, input().split())

visited = [[False for _ in range(n)] for _ in range(n)]
graph = [[] for _ in range(n)]

hos = []
for i in range(n):
    temp = input().split()
    for j in range(n):
        graph[i].append(int(temp[j]))
        if int(temp[j]) == 2:
            hos.append((i,j))
dx, dy = [0,0,-1,1], [-1,1,0,0]

count = -1
def bfs(s):
    temp_len = 0
    global count
    q = deque()
    for ss in s:
        q.append((ss[0],ss[1]))
        visited[ss[0]][ss[1]] = True
    len_q = len(q)
    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if new_x >=0 and new_x < n and new_y >=0 and new_y <n and graph[new_x][new_y] ==0 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                q.append((new_x, new_y))
        temp_len += 1
        # print(x,y)
        if temp_len >= len_q:
            count += 1
            len_q = len(q)
            temp_len = 0
            # print(count, len_q, 000000000000000000000)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and not visited[i][j]:
                count = -99



comb = list(itertools.combinations(hos, m))
min_count = 999
tp = 0
# comb = [((0, 2), (2, 4), (5, 2))]
for s in comb:
    bfs(s)
    if count < min_count:
        if count != -99:
            min_count = count
    count = -1
    visited = [[False for _ in range(n)] for _ in range(n)]

if min_count == min_count:
    print(-1)
else:
    print(min_count)

# 0 = 바이러스
# 1 = 벽
# 2 = 병원