class Queue:
    def __init__(self, size=None):
        self.size = size
        self.front = self.rear = -1
        self.arr = []

    def enqueue(self, element):
        if len(self.arr) == self.size:
            print("Overflow")
            return
        elif self.front == -1:
            self.arr.append(element)
            self.front = self.rear = 0
            return
        self.arr.append(element)
        self.rear = len(self.arr) - 1
        return

    def dequeue(self):
        if self.arr is None:
            print("Underflow")
            return
        self.arr.pop(self.front)
        return

    def printQueue(self):
        if self.arr is None:
            print("Queue is Empty")
            return
        print(self.arr)
        return


q = Queue(5)
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.dequeue()
q.dequeue()
q.printQueue()
