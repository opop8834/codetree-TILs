from collections import deque

class Deque:
    def __init__(self):
        self.dequ = deque()
    def push_front(self, value):
        self.dequ.appendleft(value)
    def push_back(self, value):
        self.dequ.append(value)
    def pop_front(self):
        if len(self.dequ) != 0:
            return self.dequ.popleft()
    def pop_back(self):
        if len(self.dequ) != 0:
            return self.dequ.pop()
    def size(self):
        return len(self.dequ)
    def empty(self):
        if len(self.dequ) != 0:
            return 0
        else:
            return 1
    def front(self):
        return(self.dequ[0])
    def back(self):
        return(self.dequ[-1])

temp_deque = Deque()
num = int(input())
for i in range(num):
    text = input()
    if "push_front" in text:
        text = text.replace("push_front ", "")
        temp_deque.push_front(text)
    elif "push_back" in text:
        text = text.replace("push_back ", "")
        temp_deque.push_back(text)
    elif "pop_front" in text:
        print(temp_deque.pop_front())
    elif "pop_back" in text:
        print(temp_deque.pop_back())
    elif "size" in text:
        print(temp_deque.size())
    elif "empty" in text:
        print(temp_deque.empty())
    elif "front" in text:
        print(temp_deque.front())
    elif "back" in text:
        print(temp_deque.back())