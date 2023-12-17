def merge_sort(array):
    """
    Sort the array using the Merge sort algorithm
    
    Parameters:
    - array: The array to be sorted
    
    Returns: The sorted array.
    """
    # If array has only 1 element, it is sorted
    if len(array) <= 1:
        return array

    # Calculate the midpoint
    midpoint = len(array) // 2

    # Call recursively on the two half arrays
    first_half = merge_sort(array[:midpoint])
    second_half = merge_sort(array[midpoint:])

    # Merge the two sorted halves
    first_index = second_index = 0
    merged_array = []

    # Merge loop
    while first_index < len(first_half) and second_index < len(second_half):
        first_value = first_half[first_index]
        second_value = second_half[second_index]

        # Choose the smaller of the two values
        if first_value < second_value:
            merged_array.append(first_value)
            first_index += 1
        else:
            merged_array.append(second_value)
            second_index += 1

    # Add the remaining elements from both halves
    if first_index < len(first_half):
        merged_array.extend(first_half[first_index:])
    elif second_index < len(second_half):
        merged_array.extend(second_half[second_index:])

    return merged_array
