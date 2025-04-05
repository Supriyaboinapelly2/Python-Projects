import math

def is_prime(n):
    """
    Checks if a given number is prime.

    Args:
        n: The number to check for primality.

    Returns:
        True if n is prime, False otherwise.
    """
    # Handle edge cases
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 1:
        return False  # 1 and numbers less than 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime

    # Optimized primality check
    # Iterate only up to the square root of n
    # Check for divisibility by numbers of the form 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
numbers_to_check = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 23, 29, 101, 1000, 10000, -5, 1.5]
for num in numbers_to_check:
    try:
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
    except TypeError as e:
        print(f"Error: {e} for input {num}")
