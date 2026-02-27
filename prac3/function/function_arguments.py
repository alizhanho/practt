# Positional argument
def multiply(a, b):
    return a * b


# Default argument
def power(base, exponent=2):
    return base ** exponent


# Multiple parameters
def full_name(first, last):
    return f"{first} {last}"


print(multiply(3, 4))
print(power(5))
print(power(2, 3))
print(full_name("Era", "isa"))