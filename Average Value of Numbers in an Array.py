def calculate_average(numbers):
  """
  Calculates the average of a list of numbers.

  Args:
    numbers: A list containing numerical values (integers or floats).

  Returns:
    The average of the numbers in the list.
    Returns 0 if the list is empty to avoid division by zero error.
  """
  # Check if the list is empty
  if not numbers:
    print("Warning: The list is empty. Returning 0 as the average.")
    return 0

  # Calculate the sum of all numbers in the list
  total_sum = sum(numbers)

  # Get the count of numbers in the list
  count = len(numbers)

  # Calculate the average
  average = total_sum / count

  return average

# --- Example Usage ---

# 1. Example with a list of integers
my_numbers = [10, 20, 30, 40, 50]
avg = calculate_average(my_numbers)
print(f"The list is: {my_numbers}")
print(f"The average is: {avg}") # Output: 30.0

print("-" * 20) # Separator

# 2. Example with a list containing floats
my_floats = [2.5, 5.0, 7.5, 10.0]
avg_floats = calculate_average(my_floats)
print(f"The list is: {my_floats}")
print(f"The average is: {avg_floats}") # Output: 6.25

print("-" * 20) # Separator

# 3. Example with an empty list
empty_list = []
avg_empty = calculate_average(empty_list)
print(f"The list is: {empty_list}")
print(f"The average is: {avg_empty}") # Output: Warning message and 0