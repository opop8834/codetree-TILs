n,m = input().split()
n = int(n)
m = int(m)

arr = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    text = input().split()
    for j in range(n):
        arr[i][j] = int(text[j])
mid = 0
mid_second = 0
count = 0
max_answer_count = -99
for k in range(n):
    mid = 0
    mid_second = 0
    count = 0
    while(True):  # 중심 정하기
        if mid < n:
            len_x = 0
            len_y = 0
            count = 0
            while(True):  # 중심에서 거리 계산
                if len_x < n:
                    cen_len_x = len_x - mid
                    cen_len_y = len_y - mid_second
                    if abs(cen_len_x)+abs(cen_len_y) <= k:
                        count += arr[len_x][len_y]
                    len_x += 1
                else:
                    len_x = 0
                    len_y += 1
                    if len_y > n-1:
                        break
            sum = k*k + (k+1) * (k+1)
            gold_cost = m * count
            cost = gold_cost - sum
            if cost >= 0 :
                if count > max_answer_count:
                    max_answer_count = count
            mid += 1
        else:
            mid = 0
            mid_second +=1
            if mid_second > n-1:
                break
            
    
print(max_answer_count)