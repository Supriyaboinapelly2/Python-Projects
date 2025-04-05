def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.
        Returns 1 if n is 0.
        Raises a ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1  # Base case: 0! = 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def factorial_recursive(n):
    """
    Calculates the factorial of a non-negative integer using recursion.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.
        Returns 1 if n is 0.
        Raises a ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1  # Base case: 0! = 1
    elif n == 1: #added another base case for 1!
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
num = 5
print(f"Factorial of {num} (iterative): {factorial(num)}")
print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")

num = 0
print(f"Factorial of {num} (iterative): {factorial(num)}")
print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")

num = 1
print(f"Factorial of {num} (iterative): {factorial(num)}")
print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")

try:
    num = -1
    print(f"Factorial of {num} (iterative): {factorial(num)}")
except ValueError as e:
    print(f"Error (iterative): {e}")

try:
    num = -1
    print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")
except ValueError as e:
    print(f"Error (recursive): {e}")

try:
    num = 3.14
    print(f"Factorial of {num} (iterative): {factorial(num)}")
except TypeError as e:
    print(f"Error (iterative): {e}")

try:
    num = 3.14
    print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")
except TypeError as e:
    print(f"Error (recursive): {e}")
