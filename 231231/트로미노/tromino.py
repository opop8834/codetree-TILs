n,m = input().split()
n = int(n)
m = int(m)

arr = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    text = input().split()
    for j in range(m):
        arr[i][j] = int(text[j])
        

max_count = -99
count = 0
first = 0
second = 0
while(True):
    count = 0
    if second+2 < m :
        count += arr[first][second]
        count += arr[first][second+1]
        count += arr[first][second+2]
        if max_count < count:
            max_count = count
        second += 1
    else:
        first += 1
        second = 0
        if first > n-1:
            break
count = 0
first = 0
second = 0
while(True):
    count = 0
    if first+2 < n :
        count += arr[first][second]
        count += arr[first+1][second]
        count += arr[first+2][second]
        if max_count < count:
            max_count = count
        first += 1
    else:
        second += 1
        first = 0
        if second > m-1:
            break
count = 0
first = 0
second = 0
while(True):
    count = 0
    if first+1 <n:
        if second+1 < m:
            count += arr[first][second]
            count += arr[first][second+1]
            count += arr[first+1][second]
            count += arr[first+1][second+1]
            temp_count = count - arr[first][second]
            if temp_count > max_count:
                max_count = temp_count
            temp_count = count - arr[first][second+1]
            if temp_count > max_count:
                max_count = temp_count
            temp_count = count - arr[first+1][second]
            if temp_count > max_count:
                max_count = temp_count
            temp_count = count - arr[first+1][second+1]
            if temp_count > max_count:
                max_count = temp_count
            second += 1
        else:
            second = 0
            first += 1 
    else:
        break
    
print(max_count)