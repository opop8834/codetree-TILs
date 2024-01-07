arr = input()
arr = list(arr)
min_count = 99
tp = 0
for s in arr:
    pre_number = arr[0]
    count = 2
    for i in range(len(arr)):
        # print("--------------------------------")
        # print(pre_number + " "+arr[i])
        # print("--------------------------------")
        if pre_number != arr[i]:
            count += 2
            tp =1
        pre_number = arr[i]
    if count < min_count:
        min_count = count
    temp_arr = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp_arr
if tp == 0:
    min_count = 3
print(min_count)