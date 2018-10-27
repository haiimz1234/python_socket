import threading
class Stack:
     def __init__(self):
         self.items = []
         self.lock = threading.Lock()



     def push(self, item):
        self.lock.acquire()
        try:
            self.items.append(item)
        finally:
            self.lock.release()

     def append(self, item):
        self.lock.acquire()
        try:
            self.items.append(item)
        finally:
            self.lock.release()

     def pop(self):
        self.lock.acquire()
        item=''
        try:
            item=self.items.pop()
        finally:
            self.lock.release()
        return item

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
        ans=0
        self.lock.acquire()
        try:
            ans= len(self.items)
        finally:
            self.lock.release()
        return ans
