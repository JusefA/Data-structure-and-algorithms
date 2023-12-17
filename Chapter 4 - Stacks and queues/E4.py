class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._size = 0
        self._front = None
        self._rear = None

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = []
        current = self._front
        while current:
            values.insert(0, str(current.data))
            current = current.next
        return f'<Queue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        new_node = ListNode(data)
        if self._rear is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        if self._front is None:
            return None

        data = self._front.data
        self._front = self._front.next
        self._size -= 1

        if self._front is None:
            self._rear = None

        return data
