from __future__ import annotations
import ctypes

class ReservedMemory():
    """
    A class to reserve and handle a contigous area of memory. The
    constructor needs the size of the memory area (in bytes) to be
    reserved.
    """
    def __init__(self, size: int) -> None:
        """
        Initialize object allocating a memory area of given size
        """
        if not isinstance(size, int):
            raise(TypeError('Memory size must be a positive integer > 0!'))
        if not 1 <= size <= 65536:
            raise(ValueError('Reserved memory size must be between 1 and 65536 bytes!'))

        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def __repr__(self) -> str:
        """
        Custom representation of the reserved memory area
        """
        l = len(self._reserved_memory)
        plural = 's' if l>1 else ''
        str_repr = f"[{', '.join(str(ord(i)) for i in self._reserved_memory)}]"
        return f"ReservedMemory ({l} byte{plural}): {str_repr}"

    def copy(self, mem_source:ReservedMemory, count:int=None, source_index:int=0, destination_index:int=0) -> None:
        """
        Copy the content of another ReservedMemory object (mem_source)
        to this object's memory area. By default the whole source memory
        area is copied to the start of this object's memory area.

        Parameters:
        - mem_source: ReservedMemory source object (mandatory)
        - count: How many bytes or positions to copy.
                Optional. Default: Source size - source_index
                If not provided, copy from the beginning or source_index
                until the end of source.
        - source_index: Source's start index or from where to copy the
                        content.
                        Optional. Default: 0
        - destination_index: Destination's start index or where to copy
                            the content.
                            Optional. Default: 0

        Usage example:
        # Copy source to the start of destination
        destination.copy(source)

        # Copy only 5 memory positions of source
        destination.copy(source, count=5)
        # or
        destination.copy(source, 5)

        # Copy source to destination starting at index 10
        destination.copy(source, destination_index=10)

        # Copy the first 5 memory positions of source to destination's index 10
        destination.copy(source, count=5, destination_index=10)

        # Copy 5 memory positions from source index 7 to destination's
        # index 10
        destination.copy(source, count=5, source_index=7, destination_index=10)
        # or
        destination.copy(source, 5, 7, 10)

        Copy area can't fall outside the bounds of the destination's
        memory area.
        """

        if not isinstance(mem_source, ReservedMemory):
            return TypeError('Source object must be a ReservedMemory object')

        if count is None:
            count = len(mem_source._reserved_memory) - source_index
        elif not isinstance(count, int):
            return TypeError('Count must be a positive integer > 0')
        elif count <= 0:
            return ValueError('Count must be a positive integer > 0')

        if not isinstance(source_index, int):
            return TypeError('Source index must be a positive integer >= 0')
        elif 0 > source_index >= len(mem_source._reserved_memory):
            return IndexError('Source index out of bounds!')

        if not isinstance(destination_index, int):
            return TypeError('Destination index must be a positive integer >= 0')
        elif 0 > destination_index >= len(self._reserved_memory):
            return IndexError('Destination index out of bounds!')

        if count > len(self._reserved_memory):
            return IndexError('Source is bigger than destination!')
        elif source_index + count > len(mem_source._reserved_memory):
            return IndexError('Source copy area out of bounds!')
        elif destination_index + count > len(self._reserved_memory):
            return IndexError('Destination copy area out of bounds!')

        self._reserved_memory[destination_index:destination_index+count] = mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k:int) -> int:
        """
        Return value at index k
        """
        if not isinstance(k, int):
            raise TypeError('Index must be a positive integer >= 0')
        elif not 0 <= k < len(self._reserved_memory):
            raise IndexError('Index is out of bounds!')

        return ord(self._reserved_memory[k])

    def __setitem__(self, k:int, val:int) -> None:
        """
        set value at index k with val
        """
        if not isinstance(k, int):
            raise TypeError('Index must be a positive integer >= 0')
        elif not (0 <= k < len(self._reserved_memory)):
            raise IndexError('Index is out of bounds!')

        self._reserved_memory[k] = val

class IntArray():
    """
    A class to implement an Array Data Structure that accepts integer values
    between -(2**(n-1)) and (2**(n-1))-1 (being n the number of bits per element).
    By default, element size is 2 bytes (16 bits), so accepted values go
    from -(2**15) to (2**15)-1, that is from -32768 to 32767.
    Python does not have a internal type with these characteristics, so values
    are accepted as normal Python int type and then converted to be stored.

    IntArray uses static arrays to hold the values, but allows to expand or
    shrunk the array internally copying the values to a new static array.

    Parameters (IntArray creation):
    - bytes_per_element: How many bytes per element should be reserved.

    Supported methods:
    - Array creation
    - Append: Insert at the end
    - Pop: Delete from the end
    """

    def __init__(self, bytes_per_element:int = 2) -> None:
        self._resmem = None
        self._size = 0  # Logical size
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2**((self._bytes_per_element * 8)-1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            self._iter_index += 1
            return self.__getitem__(self._iter_index-1)
        else:
            raise StopIteration

    def __repr__(self) -> str:
        """
        Custom representation of the IntArray
        """
        if not self._resmem:
            return "Empty IntArray"
        l = self._size
        plural = 's' if l>1 else ''
        str_repr = f"[{', '.join(str(v) for v in self)}]"
        return f"IntArray ({l} element{plural}): {str_repr}"

    def __setitem__(self, k:int, val:int) -> None:
        """
        Set value at index k with val.
        """
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')

        # Convert or shift the value to be suitable to be stored.
        # Value to be stored must be in the positive range from 0 to (2**bits_per_element)-1
        # For 2 bytes that is from 0 to 65535
        val_to_store = val + self._shift_val
        # Store the bytes of the value in Little-endian (https://en.wikipedia.org/wiki/Endianness)
        for byte_index in range(self._bytes_per_element):
            self._resmem[k*self._bytes_per_element+byte_index] = (val_to_store >> (8*byte_index)) & 255

    def __getitem__(self, k:int) -> int:
        """
        Return value at index k
        """

        # Read stored bytes in Little-endian and restore original value
        stored_val = 0
        for byte_index in range(self._bytes_per_element):
            stored_val |= self._resmem[k*self._bytes_per_element+byte_index] << (8*byte_index)
        return (stored_val - self._shift_val)

    def append(self, val: int) -> None:
        """
        Append an element to the end of the array
        """
        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError('Value must be an integer between {self._min_val} and {self._max_val}')

        # Update array's size
        self._size += 1

        # Reserve a new memory area with the new size.
        # It is _bytes_per_element bigger than the current one
        new_resmem = ReservedMemory(self._size*self._bytes_per_element)

        # Copy the old reserved memory area (if there was one)
        if self._resmem:
            new_resmem.copy(self._resmem)

        # The new created reserved memory area will be the one to be used
        # from now on
        self._resmem = new_resmem

        # Store the new value at the end of the array
        self.__setitem__(self._size-1, val)

    def pop(self) -> int:
        """
        Remove an element from the end of the array and return its value
        """
        # Elements can not be removed from empty arrays
        if self._size == 0:
            return None

        # Get the last element's value
        val = self.__getitem__(self._size-1)

        # Decrease the size of the array
        self._size -= 1

        # Find out the need for reserved memory
        if self._size > 0:
            # if new size is still bigger than 0
            # reserve a new memory area with the new size.
            # It is _bytes_per_element smaller than the current one
            new_resmem = ReservedMemory(self._size*self._bytes_per_element)
            # And copy the old memory area (except last element)
            new_resmem.copy(self._resmem, count=self._size*self._bytes_per_element)
        else:
            # If new size is 0, there is no need to reserve memory for it
            new_resmem = None

        # Make the new memory area value the current one
        self._resmem = new_resmem

        # Return the last element's value that was stored at the beginning
        return val

    def insert(self, index: int, val: int) -> None:

        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(f'Value must be an integer between {self._min_val} and {self._max_val}')
        if not 0 <= index <= self._size:
            raise IndexError('Index is out of bounds.')

        # Increase the size of the array
        self._size += 1

        # Create a new ReservedMemory object with the new size in bytes
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        # Copy values from the old ReservedMemory to the new one, making room for the new value
        if index > 0:
            new_resmem.copy(self._resmem, count=index * self._bytes_per_element)

        # Set the new value at the specified index

        val_to_store = val + self._shift_val
        for byte_index in range(self._bytes_per_element):
            new_resmem[index * self._bytes_per_element + byte_index] = (val_to_store >> (8 * byte_index)) & 255



        if index < self._size - 1:
            new_resmem.copy(self._resmem, count=(self._size - index - 1) * self._bytes_per_element, source_index=index * self._bytes_per_element, destination_index=(index + 1) * self._bytes_per_element)



        # Update the ReservedMemory to the new one
        self._resmem = new_resmem


    def remove(self, index:int) -> int:
        if not 0 <= index <= self._size:
            raise IndexError('Index is out of bounds.')
            
        removed_value = self.__getitem__(index)

        self._size -= 1
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        if index > 0:
            new_resmem.copy(self._resmem, count=index * self._bytes_per_element)

        if index < self._size:
            new_resmem.copy(
                self._resmem, count=(self._size - index) * self._bytes_per_element,
                source_index=(index + 1) * self._bytes_per_element,
                destination_index=index * self._bytes_per_element
            )

        self._resmem = new_resmem
        return removed_value
