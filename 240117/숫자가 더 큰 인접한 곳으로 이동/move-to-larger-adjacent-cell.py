n,r,c = input().split()
n = int(n)
r = int(r) - 1
c = int(c) - 1
arr = [[0 for i in range(n)] for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    text = input().split()
    for j in range(n):
        arr[i][j] = int(text[j])

i = 0
j = 0
print(arr[r][c], end =' ')
while(True):
    if j >= n:
        j = 0
        i += 1
    if i >= n:
        break
    if i == r and j == c:
        for jj in range(4):
            if i+dx[jj] < n and i+dx[jj] >= 0 and j+dy[jj] < n and j+dy[jj] >= 0:
                temp_number = arr[i+dx[jj]][j+dy[jj]]
                current_number = arr[i][j]
                # print(i+dx[jj],j+dy[jj])
                # print(temp_number, current_number)
                if (temp_number > current_number):
                    print(temp_number, end = ' ')
                    r = i+dx[jj]
                    c = j+dy[jj]
                    i = 0
                    j = 0
                    break
    j += 1