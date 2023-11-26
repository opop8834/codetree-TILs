# 삽입정렬

def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = key
    return arr
            
    
    
arr = []
num = int(input())
text = input().split()
for s in text:
    arr.append(int(s))
arr = insert_sort(arr)
for s in arr:
    print(s, end=' ')