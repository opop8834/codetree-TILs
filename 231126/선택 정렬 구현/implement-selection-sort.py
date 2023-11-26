# 선택정렬

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1 , len(arr)):  # 최솟값 찾기
            if arr[j] < arr[min]:
                min = j
        if arr[i]> arr[min]:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
        
    return arr

arr = []
num = int(input())
text = input().split()
for s in text:
    arr.append(int(s))
arr = selection_sort(arr)
for s in arr:
    print(s, end=' ')