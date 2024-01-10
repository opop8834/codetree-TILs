N,M = input().split()
N = int(N)
M = int(M)
arr = []
for i in range(N):
    text = int(input())
    arr.append(text)
arr = arr[::-1]
print(arr)

for i in range(arr):
    current_number = arr[i]
    for j in range(M):
        if