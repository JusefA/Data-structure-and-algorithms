Edef sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure
    
    Parameters:
    - array: The heap array
    - start: The index of the node that should be sinked.
    - end: The end of the heap inside the array. The index of the last node
    
    Returns: None
    """
    root = start

    while (2 * root + 1) <= end:
        child = 2 * root + 1  # Left child

        # Choose the larger child
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1

        # If the larger child is greater than the root, swap them
        if array[child] > array[root]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break

def heap_sort(array):
    """
    Sort the array using the Heapsort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    n = len(array)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, i, n - 1)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]  # Swap the root (max element) with the last element
        sift_down(array, 0, i - 1)  # Restore the heap property for the remaining elements
