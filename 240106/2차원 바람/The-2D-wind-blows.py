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
    r1,c1,r2,c2 = input().split()
    r1 = int(r1)-1
    c1 = int(c1)-1
    r2 = int(r2)-1
    c2 = int(c2)-1

    temp1 = arr[r1][c1]
    temp2 = arr[r1][c2]
    temp3 = arr[r2][c2]
    temp4 = arr[r2][c1]
    for j in range(c2,c1-1,-1):
        arr[r1][j] = arr[r1][j-1]
    for j in range(r2, r1+1,-1):
        arr[j][c2] = arr[j-1][c2]
    arr[r1+1][c2] = temp2
    for j in range(c1, c2-2):
        arr[r2][j] = arr[r2][j+1]
    arr[r2][c2-1] = temp3
    for j in range(r1, r2-2):
        arr[j][c1] = arr[j+1][c1]
    arr[r2-1][c1] = temp4



for i in range(N):
    for j in range(M):
        print(arr[i][j],end = ' ')
    print()