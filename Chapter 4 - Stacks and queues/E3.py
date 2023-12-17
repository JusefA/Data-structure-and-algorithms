class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = Stack()
        self._OutboundStack = Stack()

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [str(c) for c in reversed(self._InboundStack.items)]
        values.extend([str(c) for c in self._OutboundStack.items])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    

    def enqueue(self, data):
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        if self._OutboundStack.is_empty():
            while not self._InboundStack.is_empty():
                self._OutboundStack.push(self._InboundStack.pop())

        if not self._OutboundStack.is_empty():
            self._size -= 1
            return self._OutboundStack.pop()
        else:
            return None
