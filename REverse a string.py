def reverse_string(s):
  """Reverses a given string.

  Args:
    s: The string to reverse.

  Returns:
    The reversed string.
  """
  return s[::-1]


my_string = "hello"
reversed_string = reverse_string(my_string)
print(reversed_string)  # Output: olleh

my_string2 = "python"
reversed_string2 = reverse_string(my_string2)
print(reversed_string2) #output: nohtyp

my_string3 = ""
reversed_string3 = reverse_string(my_string3)
print(reversed_string3) #output: ""

my_string4 = "supriya"
reversed_string4 = reverse_string(my_string4)
print(reversed_string4) #output: a