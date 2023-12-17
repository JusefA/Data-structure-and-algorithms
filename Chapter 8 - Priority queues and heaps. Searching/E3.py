def binary_search_iterative(array, value):
    """
    Performs a binary search in the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    low, high = 0, len(array) - 1  # Initialize the search area

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index

        if array[mid] == value:
            return mid  # Value found, return the index
        elif array[mid] < value:
            low = mid + 1  # Adjust the search area to the right half
        else:
            high = mid - 1  # Adjust the search area to the left half

    return None  # Value not found
