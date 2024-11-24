# Очередь

class Queue:
    
    lst = []
    
    def push(self, item):
        self.lst.append(item)
    
    def pop(self):
        return self.lst.pop(0)
    
    def is_empty(self):
        return self.lst == []
    

queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
