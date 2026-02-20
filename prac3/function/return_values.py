def get_max(numbers):
    """Returns maximum number from list."""
    return max(numbers)


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print(get_max([3, 7, 2, 18]))
print(divide(10, 2))
print(divide(5, 0))