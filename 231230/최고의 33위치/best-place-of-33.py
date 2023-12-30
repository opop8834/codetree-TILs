num = input()
num = int(num)
arr = [[0 for j in range(num)] for i in range(num)]

for i in range(num):
    text = input().split()
    for j in range(num):
        arr[j][i] = int(text[j])

one = 0
second = 0

count = 0
max_count = -99
while(True):
    if one+2 >= len(arr):
        second += 1
        one = 0
    if second+2 >= len(arr):
        break
    else:
        count += arr[one][second]
        count += arr[one+1][second]
        count += arr[one+2][second]
        count += arr[one][second+1]
        count += arr[one+1][second+1]
        count += arr[one+2][second+1]
        count += arr[one][second+2]
        count += arr[one+1][second+2]
        count += arr[one+2][second+2]
    if count > max_count:
        max_count = count
    count = 0
    one += 1
print(max_count)