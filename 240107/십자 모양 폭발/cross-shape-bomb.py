n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
temp_arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    text = input().split()
    for j in range(n):
        arr[i][j] = int(text[j])

for i in range(n):
    for j in range(n):
        temp_arr[i][j] = arr[i][j]
r,c = input().split()
r = int(r) - 1
c = int(c) - 1

center = arr[r][c]
len_center = center-1
for i in range(n):
    for j in range(n):
        if i == r and j >= c-len_center and j <= c + len_center:
            temp_arr[i][j] = 0
        elif j == c and i >= r-len_center and i <= r+len_center:
            temp_arr[i][j] = 0

tp_arr = []
count = 0
for i in range(n):
    for j in range(n-1,-1,-1):
        if temp_arr[j][i] != 0:
            tp_arr.append(temp_arr[j][i])
        else:
            count +=1
    for j in range(count):
        tp_arr.append(0)
    count = 0
for i in range(n-1,-1,-1):
    for j in range(n):
        print(tp_arr[j*n + i], end=' ')
    print()