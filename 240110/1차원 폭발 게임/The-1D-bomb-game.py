N,M = input().split()
N = int(N)
M = int(M)
arr = []
for i in range(N):
    text = int(input())
    arr.append(text)
arr = arr[::-1]

for kk in range(N):
    temp_arr = []
    i = 0
    while(i <= len(arr)-1):
        tp = 0
        count = 1
        current_number = arr[i]
        while(True):
            if i+count <= len(arr)-1 and current_number == arr[i+count]:
                count += 1
            else:
                if count >= M:
                    tp = 1
                break
        if tp == 1:
            i += count
            count = 1
            tp = 0
        else:
            temp_arr.append(current_number)
            i+=1
    arr.clear()
    for ii in range(len(temp_arr)):
        arr.append(temp_arr[ii])

arr = arr[::-1]
print(len(arr))
if len(arr) != 0:
    for i in range(len(arr)):
        print(arr[i])