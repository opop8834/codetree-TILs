n = int(input())

count = list(map(int, input().split()))


# 팀장 최대 , 팀원 최대
owner, team = map(int,input().split())
sum_ = 0
for s in count:
    if s > owner:
        temp = s - owner
        temp_2 = int(temp / team)
        if temp % team> 0:
            temp_2 += 1
            
        # 팀장 까지 합
        temp_2 += 1    
        sum_ += temp_2
    else:
        sum_ += 1
print(sum_)