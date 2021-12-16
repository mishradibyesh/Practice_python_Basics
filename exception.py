"""
Exception : An exception is an event,
which occurs during the execution of a program that disrupts the normal
flow of the program's instructions.
"""
try:
    k = 5 / 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')