def push_back(list, A):
    list.append(A)
    return list

def pop_back(list):
    list.pop()
    return list

def size(list):
    return len(list)

def get(list,K):
    return list[K-1]


N = int(input())
list = []
for i in range(N):
    text = input()
    if " " in text:
        text,key = text.split()
        key = int(key)
    if text == "push_back":
        list = push_back(list,key)
    elif text == "get":
        t1 = get(list,key)
        print(t1)
    elif text == "size":
        t2 = size(list)
        print(t2)
    elif text == "pop_back":
        list = pop_back(list)