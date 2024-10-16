import itertools

n = int(input())
temp = list(map(int,input().split()))
cal = list(map(int,input().split()))

max_ = -9999
min_ = 9999

cal_str = []
for i in range(cal[0]):
    cal_str.append("+")
for i in range(cal[1]):
    cal_str.append("-")
for i in range(cal[2]):
    cal_str.append("*")

comb = list(itertools.permutations(cal_str,n-1))

result = []
for value in comb:
    if value not in result:
        result.append(value)

# print(result)

for s in result:
    sum_ = temp[0]
    for i in range(1,len(temp)):
        if s[i-1] == '+':
            sum_ += temp[i]
        if s[i-1] == '-':
            sum_ -= temp[i]
        if s[i-1] == '*':
            sum_ *= temp[i]
    if sum_ < min_:
        min_ = sum_
    if sum_ >= max_:
        max_ = sum_
print(min_, max_)