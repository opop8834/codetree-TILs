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
            dxs = i+dx[jj]
            dys = j+dy[jj]
            # print(dxs, dys)
            if dxs<n and dxs>=0 and dys<n and dys>=0:
                temp_number = arr[dxs][dys]
                current_number = arr[i][j]
                # print(dxs,dys)
                # print(temp_number, current_number)
                if (temp_number > current_number):
                    print(temp_number, end = ' ')
                    r = dxs
                    c = dys
                    i = 0
                    j = -1
                    break
    j += 1