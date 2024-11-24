# Стек

class Stack:
    lst = []
    
    def push(self, item):
        self.lst.append(item)
    
    def pop(self):
        return self.lst.pop()
    
    def is_empty(self):
        return self.lst == []
    

stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
