num, m = input().split()
num = int(num)
m = int(m)

arr = [[0 for j in range(num)] for i in range(num)]

for i in range(num):
    text = input().split()
    for j in range(num):
        arr[j][i] = int(text[j])

prev = -99
ins = -99
count = 1
answer = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if j == 0:
            prev = arr[j][i]
        else:
            ins = arr[j][i]
        if prev == ins:
            count += 1
        if count == m:
            answer += 1
            count = 1
            break
        prev = arr[j][i]
    count = 1
count = 1
prev = -99
ins = -99
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == 0:
            prev = arr[i][j]
        else:
            ins = arr[i][j]
        if prev == ins:
            count += 1
        if count == m:
            answer += 1
            count = 1
            break
        prev = arr[i][j]
    count = 1
print(answer)