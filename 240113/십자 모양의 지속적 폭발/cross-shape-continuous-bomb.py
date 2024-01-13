N,M = input().split()
N = int(N)
M = int(M)

arr = [[0 for j in range(N)] for i in range(N)]
temp_arr = [[0 for j in range(N)] for i in range(N)]
for i in range(N):
    text = input().split()
    for j in range(N):
        arr[i][j] = int(text[j])

for cc in range(M):
    c = int(input())
    c= c-1  # 선택 열
    center_x = 0
    center_num = -99
    for count in range(N):
        center_num = arr[center_x][c]
        center_num = center_num - 1 # 거리
        if center_num == -1:
            center_x += 1
        else:
            break
    if center_num == -1:
        continue
    else:
        for i in range(N):
            for j in range(N):
                if i ==center_x and j >= c - center_num and j <= c + center_num:
                    temp_arr[i][j] = 0
                elif i != center_x and i <= center_x + center_num and j == c: 
                    temp_arr[i][j] = 0
                else:
                    temp_arr[i][j] = arr[i][j]
        for i in range(N):
            tp = 0
            for j in range(N-1,0,-1):
                current_number = temp_arr[j][i]
                if current_number == 0 and tp == 0:
                    tp = 1
                    temp_arr[j][i] = temp_arr[j-1][i]
                elif tp == 1:
                    temp_arr[j][i] = temp_arr[j-1][i]
            if tp == 1:
                temp_arr[0][i] = 0
        for i in range(N):
            for j in range(N):
                arr[i][j] = temp_arr[i][j]
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()