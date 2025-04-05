def find_max(arr):
    """
    Finds the maximum number in an array (list).

    Args:
        arr: A list of numbers.

    Returns:
        The maximum number in the array, or None if the array is empty.
    """
    if not arr:  # Check if the array is empty
        return None
    max_num = arr[0]  # Initialize max_num with the first element
    for num in arr:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found
    return max_num

# Example usage:
numbers1 = [1, 5, 2, 8, 3]
max_number1 = find_max(numbers1)
print(f"The maximum number in {numbers1} is {max_number1}")  # Output: 8

numbers2 = [-2, -5, -1, -9, -3]
max_number2 = find_max(numbers2)
print(f"The maximum number in {numbers2} is {max_number2}")  # Output: -1

numbers3 = [0, 0, 0, 0, 0]
max_number3 = find_max(numbers3)
print(f"The maximum number in {numbers3} is {max_number3}")  # Output: 0

numbers4 = []
max_number4 = find_max(numbers4)
print(f"The maximum number in {numbers4} is {max_number4}")  # Output: None

numbers5 = [100, 200, 50, 60, 150]
max_number5 = find_max(numbers5)
print(f"The maximum number in {numbers5} is {max_number5}")
