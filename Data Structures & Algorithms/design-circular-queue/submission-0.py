class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for i in range(k)]
        self.front = 0
        self.rear = 0
        self.k = k
        self.size = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear += 1
        self.rear %= self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        self.front %= self.k
        self.size -= 1
        return True
    

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear - 1]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        print(self.queue)
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()