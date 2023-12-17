class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        return self._top.data if self._top else None

    def push(self, data):
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        if self._top:
            popped_data = self._top.data
            self._top = self._top.next
            self._size -= 1
            return popped_data
        else:
            return None

    def __repr__(self):
        elements = ', '.join(str(node.data) for node in self)
        return f'<Stack ({self._size} element{"s" if self._size != 1 else ""}): [{elements}]>'

    def __iter__(self):
        current = self._top
        while current:
            yield current
            current = current.next
