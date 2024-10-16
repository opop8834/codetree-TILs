import itertools
import sys

n = int(input())
temp = list(map(int,input().split()))
cal = list(map(int,input().split()))

max_ = -sys.maxsize
min_ = sys.maxsize

cal_str = []
for i in range(cal[0]):
    cal_str.append("+")
for i in range(cal[1]):
    cal_str.append("-")
for i in range(cal[2]):
    cal_str.append("*")

comb = set(itertools.permutations(cal_str,n-1))

result = comb

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
    # print(sum_)
    if sum_ < min_:
        min_ = sum_
    if sum_ >= max_:
        max_ = sum_
print(min_, max_)