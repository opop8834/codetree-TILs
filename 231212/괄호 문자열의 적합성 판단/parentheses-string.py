class Stack:
    def __init__(self):
        self.st = []
    def push(self,value):
        self.st.append(value)
    def pop(self):
        if len(self.st) <= 0:
            raise Exception("Stack is empty")
        self.st.pop()
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

# temp_stack = Stack()
# num = int(input())
# for i in range(num):
#     text = input()
#     if "push" in text:
#         text = text.replace("push ", "")
#         temp_stack.push(text)
#     elif "size" in text:
#         print(temp_stack.size())
#     elif "empty" in text:
#         print(temp_stack.empty())
#     elif "pop" in text:
#         print(temp_stack.pop())
#     elif "top" in text:
#         print(temp_stack.top())

temp_stack = Stack()
text = input()
tp = 0
for i in range(len(text)):
    temp = text[i]
    if "(" == temp:
        temp_stack.push(temp)
    else:
        if temp_stack.empty() == 1:
            tp = 1
            break
        else:
            temp_stack.pop()
if temp_stack.empty() == 1 and tp == 0:
    print("Yes")
else:
    print("No")