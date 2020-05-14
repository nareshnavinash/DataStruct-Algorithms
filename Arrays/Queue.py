class Queue:

    def __init__(self):
        self.data = []

    def enqueue(self,data):
        self.data.insert(0, data)

    def dequeue(self):
        return self.data.pop()

    def length(self):
        return len(self.data)

    def is_empty(self):
        return True if not self.data else False

    def first(self):
        return self.data[-1]

    def entire_array(self):
        return self.data

a = Queue()
a.enqueue("3")
a.enqueue("2")
a.enqueue("5")
a.enqueue("6")
a.enqueue("7")
a.enqueue("8")
# print(a.entire_array())
a.dequeue()
# print(a.entire_array())
