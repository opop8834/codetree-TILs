import itertools

n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    t, p = map(int,input().split())
    arr[i].append(t)
    arr[i].append(p)
    
comb = []
for i in range(1,n+1):
    comb.append(list(itertools.combinations(arr,i)))

max_p = -999
for s in comb:  # 1개의 조합, 2개의 조합 등등
    for ss in s: # ~~개의 조합 원소들을 출력
        sum_t = 0
        sum_p = 0
        for sss in ss:  # 조합 안의 원소 추출
            sum_t += sss[0]
            sum_p += sss[1]
        if sum_t <= n and sum_p > max_p:
            max_p = sum_p
            

if max_p == -999:
    print(0)
else:
    print(max_p)