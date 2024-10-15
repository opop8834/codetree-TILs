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
sum_t = 0
sum_p = 0
for s in comb:
    for ss in s:
        for sss in ss:
            sum_t += sss[0]
            sum_p += sss[1]
        if sum_t <= n and sum_p > max_p:
            max_p = sum_p
            sum_t = 0
            sum_p = 0
            

if max_p == -999:
    print(0)
else:
    print(max_p)