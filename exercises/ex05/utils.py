"""Exercise 5!"""

__author__ = "730466694"


def only_evens(even: list[int]) -> list[int]:
    """Compute the even numbers of the list."""
    even_list = []
    for item in even:
        if item % 2 == 0:
            even_list.append(item)
    return even_list


def sub(a: list[int], start_index: int, end_index: int) -> list[int]:
    """Generate a list which is a subset of the given list between the start and end index."""
    if len(a) == 0 or start_index > len(a) or end_index <= 0:
        return []
    if start_index < 0:
        start_index = 0
    if end_index > len(a):
        end_index = len(a)
    a_list = list()
    while start_index < end_index:
        a_list.append(a[start_index])
        start_index += 1
    return a_list


def concat(one_list: list[int], two_list: list[int]) -> list[int]:
    """Concatenate list one and list two."""
    b_list = []
    for item in one_list:
        b_list.append(item)
    for item in two_list:
        b_list.append(item)
    return b_list