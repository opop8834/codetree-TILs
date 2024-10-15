import itertools
n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    temp = map(int, input().split())
    for s in temp:
        graph[i].append(s)   

divide = int(n/2) 
arr = []
for i in range(1,n+1):
    arr.append(i)

com = list(itertools.combinations(arr,divide))
# print(com)
min_ = 999
for breaktime in com:
    # print(breaktime)
    dinner = list(set(arr) - set(breaktime))
    # print(dinner)
    comb= list(itertools.permutations(breaktime,2))
    # print(comb)
    comb2= list(itertools.permutations(dinner,2))
    # print(comb2)
    sum_ = 0
    for i in range(len(comb)):
        index1 = comb[i][0]
        index2 = comb[i][1]
        index1 -= 1
        index2 -= 1
        sum_ += graph[index1][index2]
    sum_2 = 0
    for i in range(len(comb2)):
        index1 = comb2[i][0]
        index2 = comb2[i][1]
        index1 -= 1
        index2 -= 1
        sum_2 += graph[index1][index2]
    if sum_2 > sum_ :
        if sum_2 - sum_ < min_:
            min_ = sum_2 - sum_
    else:
        if sum_ - sum_2 < min_:
            min_ = sum_ - sum_2
print(min_)