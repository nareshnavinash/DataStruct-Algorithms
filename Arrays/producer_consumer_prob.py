from threading import Thread, Condition
import random
import time

condition = Condition()
arr = []
MAX_LEN = 10


class Producer(Thread):
    def run(self) -> None:
        nums = range(0, 9) # to produce the random array
        global arr
        while True:
            num = random.choice(nums)
            condition.acquire()
            if len(arr) >= MAX_LEN:
                print("Waiting for consumer to take few elements from queue")
                condition.wait()
                print("Consumer given a notification that an element is removed")
            arr.append(num)
            condition.notify()
            print("Enqueued", num)
            time.sleep(random.random())
            condition.release()


class Consumer(Thread):
    def run(self) -> None:
        global arr
        while True:
            condition.acquire()
            if not arr:
                print("Waiting for producer to produce some data")
                condition.wait()
                print("Producer has produced data and notified the consumer")
            num = arr.pop()
            condition.notify()
            print("Dequeued", num)
            time.sleep(random.random())
            condition.release()


Producer().start()
Consumer().start()


