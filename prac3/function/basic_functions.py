# Example 1: Simple function
def greet(name):
    """This function greets a person by name."""
    print(f"Hello, {name}!")


# Example 2: Function returning value
def square(number):
    """Returns the square of a number."""
    return number ** 2


# Example 3: Function with list argument
def print_list(items):
    """Prints each item in a list."""
    for item in items:
        print(item)


# Example 4: Function with docstring
def is_even(number):
    """
    Checks if a number is even.
    Returns True if even, False otherwise.
    """
    return number % 2 == 0


# Test
greet("Ali")
print(square(5))
print_list(["apple", "banana", "cherry"])
print(is_even(4))