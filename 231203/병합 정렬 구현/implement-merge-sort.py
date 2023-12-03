def merge_sort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    left1 = merge_sort(left)
    right1 = merge_sort(right)
    
    return merge(left1, right1)


def merge(left, right):
    i = 0
    j = 0

    merge_arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge_arr.append(left[i])    
            i = i+1
        else:
            merge_arr.append(right[j])
            j = j+1
    while i< len(left):
        merge_arr.append(left[i])
        i = i+1
    while j < len(right):
        merge_arr.append(right[j])
        j = j+1
    
    return merge_arr

arr = []
num = int(input())
text = input().split()
for s in text:
    arr.append(int(s))
arr = merge_sort(arr)
for s in arr:
    print(s, end=' ')