n = int(input())
arr=[0]*n
for i in range(n):
    input_num = int(input())
    arr[i] = input_num
for i in range(2):
    s,e = input().split()
    s = int(s) - 1
    e = int(e) - 1
    temp_arr =[]
    j = 0
    while(j <= len(arr)-1):
        if j == s:
            j += e-s
        else:
            temp_arr.append(arr[j])
        j += 1
    arr = []
    for j in range(len(temp_arr)):
        arr.append(temp_arr[j])

print(len(arr))
for i in range(len(arr)):
    print(arr[i])