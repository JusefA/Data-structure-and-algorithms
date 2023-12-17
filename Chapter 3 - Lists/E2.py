class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        new_node = ListNode(value)

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def pop(self):
        """
        Remove and return the last element from the list

        Returns:
        - The value of the removed element or None if the list is empty
        """
        if self._size == 0:
            return None
        elif self._size == 1:
            value = self._head.data
            self._head = self._tail = None
        else:
            current_node = self._head
            while current_node.next != self._tail:
                current_node = current_node.next

            value = self._tail.data
            self._tail = current_node
            current_node.next = None

        self._size -= 1
        return value
