class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    pairs = []

    for num in numbers:
        if num % 2 == 0:  # even number
            if not odd_queue.is_empty():
                odd_num = odd_queue.dequeue()
                pairs.append((num, odd_num))
            else:
                even_queue.enqueue(num)
        else:  # odd number
            if not even_queue.is_empty():
                even_num = even_queue.dequeue()
                pairs.append((even_num, num))
            else:
                odd_queue.enqueue(num)

    return pairs

