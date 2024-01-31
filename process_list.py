def process_integer_list(input_list):
    """
    Process a list of integers based on the following criteria:
    1. Accepts a list of integers.
    2. Emits an error message if the list is not a multiple of 10 in length.
    3. Returns a new list with items at positions that are multiples of 2 or 3 removed.

    Args:
        input_list (list): A list of integers.

    Returns:
        list: A new list with items at positions that are multiples of 2 or 3 removed.

    Raises:
        ValueError: If the length of the input list is not a multiple of 10.
    """
    # Check if the length of the list is a multiple of 10
    if len(input_list) % 10 != 0:
        raise ValueError("Error: The length of the list must be a multiple of 10.")

    # Filter the list to remove items at positions that are multiples of 2 or 3
    result_list = [num for idx, num in enumerate(input_list) if (idx + 1) % 2 != 0 and (idx + 1) % 3 != 0]

    return result_list

