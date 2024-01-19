n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k) - 1

arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    text = input().split()
    for j in range(n):
        arr[i][j] = int(text[j])

temp_range = k + m - 1
for i in range(n-1, -1, -1):
    tp = 0
    for j in range(k,temp_range+1):
        current_number = arr[i][j]
        if current_number == 1:
            tp = 1
    if tp == 0:  # 0 일때 input하기 전 위에 가림막이 있는지 check
        for ii in range(i,-1,-1):
            for jj in range(k,temp_range+1):
                current_number = arr[ii][jj]
                if current_number == 1:
                    tp = 1
        if tp == 0:
            for jjj in range(k,temp_range+1):
                    arr[i][jjj] = 1
            break
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()