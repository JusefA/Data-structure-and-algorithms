class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
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
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration
            
    def __getitem__(self, index):
        """
        Return value at index
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        
        # Return the value
        return current_node.data

    def __setitem__(self, index, value):
        """
        set value at index k with val
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Set the value
        current_node.data = value

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value. This is the last node, so next is None,
        # but there can be already some node in the list, hence the prev value
        new_node = ListNode(value, next=None, prev=self._tail)

        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # In any other case, update tail node to point to the new element
            # and update tail pointer. The new node already points to its
            # previous element
            self._tail.next = new_node
            self._tail = new_node

        # update size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list
        
        Parameters: None
        
        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # If list is empty, returns None
        if not self._size:
            return None
        
        # Locate previous_node (the node just before last node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._tail:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None   # It is now the last node

        # Update tail pointer
        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value

    def contains(self, value):
        """
        Returns True if value if found in the list and False if not
        """
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        """
        Clear the list
        """
        # Remove all nodes
        current_node = self._head
        while current_node:
            next = current_node.next
            del(current_node)
            current_node = next

        # Update pointers and size
        self._head = self._tail = None
        self._size = 0

    def insert(self, index, value):
        """
        Insert a new node with value at the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        # Check if index is inside bounds
        if index < 0 or index > self._size:
            raise ValueError('Index out of bounds')

        # Create the new node with the given value
        new_node = ListNode(value)

        # Special case: insert at the front
        if index == 0:
            new_node.next = self._head
            if self._head:
                self._head.prev = new_node
            self._head = new_node

            # If the list was empty, update the tail
            if self._size == 0:
                self._tail = new_node

        else:
            # Move to the node before the one to be inserted
            previous_node = self._head
            for _ in range(index - 1):
                previous_node = previous_node.next

            # Update the pointers of the new node
            new_node.next = previous_node.next
            new_node.prev = previous_node

            # Update the pointers of the surrounding nodes
            if previous_node.next:
                previous_node.next.prev = new_node
            previous_node.next = new_node

            # If inserting at the end, update the tail
            if new_node.next is None:
                self._tail = new_node

        # Update the size of the list
        self._size += 1

