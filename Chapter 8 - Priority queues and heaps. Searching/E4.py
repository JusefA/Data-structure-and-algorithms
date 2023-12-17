def interpolation_search(array, value):
    """
    Performs an Interpolation search in the array for the given value
    
    Parameters:
    - array: The array where to perform the search
    - value: The value being searched
    
    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    low, high = 0, len(array) - 1

    while low <= high and array[low] <= value <= array[high]:
        # Calculate the probable position based on the value and array elements
        denominator = array[high] - array[low]
        if denominator == 0:
            # Avoid division by zero
            pos = low if array[low] == value else None
        else:
            pos = low + ((high - low) // denominator) * (value - array[low])

        if pos is not None and array[pos] == value:
            return pos  # Value found, return the index
        elif array[pos] < value:
            low = pos + 1  # Adjust the search area to the right
        else:
            high = pos - 1  # Adjust the search area to the left

    return None  # Value not found

