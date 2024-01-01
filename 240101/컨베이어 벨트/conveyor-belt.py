n,t = input().split()
n = int(n)
t = int(t)
text = input().split()
arr = [[0 for i in range(n)] for j in range(2)]

for i in range(n):
    arr[0][i] = int(text[i])
text = input().split()
for i in range(n):
    arr[1][i] = int(text[i])

# 뒷 리스트 맨뒤 추출 temp_1
# 앞 리스트 앞에 추가 temp_1  -> 앞 리스트 맨뒤 추출 temp_2 
# 뒷 리스트 앞에 추가 temp_2
for i in range(t):
    temp_1 = arr[1][-1]
    temp_2 = arr[0][-1]
    for j in range(len(arr), 0, -1):
        arr[0][j] = arr[0][j-1]
        arr[1][j] = arr[1][j-1]
    arr[0][0] = temp_1
    arr[1][0] = temp_2
for i in range(2):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')
    print()