def sift_down(array, start, end):
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
