from collections import deque

class Queue:
    def __init__(self):
        self.qu = deque()
    def push(self, value):
        self.qu.append(value)
    def pop(self):
        return (self.qu.popleft())
    def size(self):
        return len(self.qu)
    def empty(self):
        if len(self.qu) == 0:
            return 1
        else:
            return 0
    def front(self):
        if len(self.qu) == 0:
            raise Exception("Queue is empty")
        return self.qu[0]
        
# temp_queue = Queue()
# num = int(input())
# for i in range(num):
#     text = input()
#     if "push" in text:
#         text = text.replace("push ", "")
#         temp_queue.push(text)
#     elif "size" in text:
#         print(temp_queue.size())
#     elif "empty" in text:
#         print(temp_queue.empty())
#     elif "pop" in text:
#         print(temp_queue.pop())
#     elif "front" in text:
#         print(temp_queue.front())
        
temp_queue = Queue()
N, K = input().split(" ")
N = int(N)
K = int(K)  
for i in range(1,N+1):
    temp_queue.push(i)

while temp_queue.size() >=1:
    for j in range(K-1):
        temp_queue.push(temp_queue.front())
        temp_queue.pop()
    print(temp_queue.pop(), end=" ")