arr = [[0 for i in range(4)]for j in range(4)]
temp_arr = [[0 for i in range(4)]for j in range(4)]

for i in range(4):
    text = input().split()
    for j in range(4):
        arr[i][j] = int(text[j])
# 두번만 합치기

instruct = input()
if instruct == 'L':
    for i in range(len(arr)):
        j = 0
        temp_j = 0
        first_number = -99
        second_number = -99
        while (True):
            if j >= len(arr[i]):
                if first_number != -99:
                    temp_arr[i][temp_j] = first_number
                    for jj in range(temp_j+1,4):
                        temp_arr[i][jj] = 0
                else:
                    for jj in range(temp_j,4):
                        temp_arr[i][jj] = 0
                break
            if arr[i][j] !=0 and first_number == -99:
                first_number = arr[i][j]
            elif arr[i][j] == 0 and first_number == -99:
                first_number = -99
            elif arr[i][j] !=0 and first_number != -99 and second_number == -99:
                second_number = arr[i][j]
                if first_number == second_number:
                    temp_arr[i][temp_j] = first_number + second_number
                    temp_j += 1
                    first_number = -99
                    second_number = -99
                else:
                    temp_arr[i][temp_j] = first_number
                    temp_j += 1
                    first_number = second_number
                    second_number = -99
            j += 1
elif instruct == 'R':
    for i in range(len(arr)):
        j = len(arr)-1
        temp_j = len(arr)-1
        first_number = -99
        second_number = -99
        while (True):
            if j < 0:
                if first_number != -99:
                    temp_arr[i][temp_j] = first_number
                    for jj in range(temp_j-1,-1,-1):
                        temp_arr[i][jj] = 0
                else:
                    for jj in range(temp_j,-1,-1):
                        temp_arr[i][jj] = 0
                break
            if arr[i][j] !=0 and first_number == -99:
                first_number = arr[i][j]
            elif arr[i][j] == 0 and first_number == -99:
                first_number = -99
            elif arr[i][j] !=0 and first_number != -99 and second_number == -99:
                second_number = arr[i][j]
                if first_number == second_number:
                    temp_arr[i][temp_j] = first_number + second_number
                    temp_j -= 1
                    first_number = -99
                    second_number = -99
                else:
                    temp_arr[i][temp_j] = first_number
                    temp_j -= 1
                    first_number = second_number
                    second_number = -99
            j -= 1
elif instruct == 'U':
    for i in range(len(arr)):
        j = 0
        temp_j = 0
        first_number = -99
        second_number = -99
        while (True):
            if j >= len(arr[i]):
                if first_number != -99:
                    temp_arr[temp_j][i] = first_number
                    for jj in range(temp_j+1,4):
                        temp_arr[jj][i] = 0
                else:
                    for jj in range(temp_j,4):
                        temp_arr[jj][i] = 0
                break
            if arr[j][i] !=0 and first_number == -99:
                first_number = arr[j][i]
            elif arr[j][i] == 0 and first_number == -99:
                first_number = -99
            elif arr[j][i] !=0 and first_number != -99 and second_number == -99:
                second_number = arr[j][i]
                if first_number == second_number:
                    temp_arr[temp_j][i] = first_number + second_number
                    temp_j += 1
                    first_number = -99
                    second_number = -99
                else:
                    temp_arr[temp_j][i] = first_number
                    temp_j += 1
                    first_number = second_number
                    second_number = -99
            j += 1
elif instruct == 'D':
    for i in range(len(arr)):
        j = len(arr)-1
        temp_j = len(arr)-1
        first_number = -99
        second_number = -99
        while (True):
            if j < 0:
                if first_number != -99:
                    temp_arr[temp_j][i] = first_number
                    for jj in range(temp_j-1,-1,-1):
                        temp_arr[jj][i] = 0
                else:
                    for jj in range(temp_j,-1,-1):
                        temp_arr[jj][i] = 0
                break
            if arr[j][i] !=0 and first_number == -99:
                first_number = arr[j][i]
            elif arr[j][i] == 0 and first_number == -99:
                first_number = -99
            elif arr[j][i] !=0 and first_number != -99 and second_number == -99:
                second_number = arr[j][i]
                if first_number == second_number:
                    temp_arr[temp_j][i] = first_number + second_number
                    temp_j -= 1
                    first_number = -99
                    second_number = -99
                else:
                    temp_arr[temp_j][i] = first_number
                    temp_j -= 1
                    first_number = second_number
                    second_number = -99
            j -= 1
for i in range(len(temp_arr)):
    for j in range(len(temp_arr)):
        print(temp_arr[i][j], end=' ')
    print()