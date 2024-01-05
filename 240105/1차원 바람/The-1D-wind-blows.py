N,M,Q = input().split()
N = int(N)
M = int(M)
Q = int(Q)

arr = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    text = input().split()
    for j in range(M):
        arr[i][j] = int(text[j])
for i in range(Q):
    r,d = input().split()
    temp_d = d
    temp_r = int(r)
    r = int(r)-1
    while(r>=0):
        if 'R' == d: # 왼쪽 shift
            temp= arr[r][0]
            for i in range(0, M-1):
                arr[r][i] = arr[r][i+1]
            arr[r][-1] = temp
            d = 'L'
        elif 'L' == d:  # 오른쪽 shift
            temp= arr[r][-1]
            for i in range(M-1, 0, -1):
                arr[r][i] = arr[r][i-1]
            arr[r][0] = temp
            d = 'R'
        if r > 0:
            tp = 0
            for i in range(M):
                if arr[r-1][i] == arr[r][i]:
                    tp = 1
            if tp != 1:
                break
        r -= 1
    r = temp_r
    if temp_d == 'L':
        d = 'R'
    else:
        d = 'L'
    while(r<=N-1):
        if 'R' == d: # 왼쪽 shift
            temp= arr[r][0]
            for i in range(0, M-1):
                arr[r][i] = arr[r][i+1]
            arr[r][-1] = temp
            d = 'L'
        elif 'L' == d:  # 오른쪽 shift
            temp= arr[r][-1]
            for i in range(M-1, 0, -1):
                arr[r][i] = arr[r][i-1]
            arr[r][0] = temp
            d = 'R'
        if r < N-1:
            tp = 0
            for i in range(M):
                if arr[r][i] == arr[r+1][i]:
                    tp = 1
            if tp != 1:
                break      
        r += 1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()