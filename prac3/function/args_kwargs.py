# *args example
def add_numbers(*args):
    """Adds any number of arguments"""
    return sum(args)


# **kwargs example
def print_info(**kwargs):
    """Prints key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print(add_numbers(1, 2, 3, 4, 5))

print_info(name="Ali", age=25, country="Kazakhstan")