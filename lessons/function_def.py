"""An Example function definiton"""

print(my_max(1, 2))

def my_max(a: int, b: int) -> int:
    """Returns the largest argument"""
    if a >= b:
        return a
    else:
        return b
print(my_max(10 + 1, 10))