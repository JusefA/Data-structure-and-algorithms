def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: Nothing. The array is sorted in-place.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Move elements greater than key to one position ahead of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Place the key in its correct position
        array[j + 1] = key
