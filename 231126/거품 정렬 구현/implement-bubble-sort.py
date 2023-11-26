# 개선된 버블정렬

def update_bubble(arr):
    arrlen = len(arr)
    state = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            state = False
        
    while state == False:
        state = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                state = False
    return arr

arr = []
num = int(input())
text = input().split()
for s in text:
    arr.append(int(s))
print(arr)
arr = update_bubble(arr)
print(arr)