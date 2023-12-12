class Stack:
    def __init__(self):
        self.st = []
    def push(self,value):
        self.st.append(value)
    def pop(self):
        if len(self.st) <= 0:
            raise Exception("Stack is empty")
        return self.st.pop()
    def size(self):
        return len(self.st)
    def empty(self):
        if len(self.st) == 0:
            return 1
        else:
            return 0
    def top(self):
        if len(self.st) <= 0:
            raise Exception("Stack is empty")
        return self.st[-1]

temp_stack = Stack()
num = int(input())
for i in range(num):
    text = input()
    if "push" in text:
        text = text.replace("push ", "")
        temp_stack.push(text)
    elif "size" in text:
        print(temp_stack.size())
    elif "empty" in text:
        print(temp_stack.empty())
    elif "pop" in text:
        print(temp_stack.pop())
    elif "top" in text:
        print(temp_stack.top())