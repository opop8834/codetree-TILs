K,N = input().split()
K = int(K)
N = int(N)
arr= []
index = 1
def recursion(index):
    if index == N+1:
        tp = 1
        for s in arr:
            print(s, end = ' ')
            if tp == N:
                print()
            tp += 1
        return
    for i in range(1,K+1):
        arr.append(i)
        recursion(index + 1)
        arr.pop()

recursion(index)