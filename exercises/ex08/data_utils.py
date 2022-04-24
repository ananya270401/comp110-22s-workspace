"""Dictionary related utility functions."""

__author__ = "730466694"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_data: dict[int, list[int]], x: int) -> dict[int, list[int]]:
    """Produce a new column based table with only the first rows of data for each column."""
    return_dict: dict[int, list[int]] = {}
    if x > len(column_data):
        x = len(column_data)
    for i in column_data:
        item = []
        item_2: list[int] = column_data[i]
        for z in range(x):
            item.append(item_2[z])
        return_dict[i] = item
    return return_dict


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for i in names:
        result[i] = table[i]
    return result


def concat(table: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for i in table:
        result[i] = table[i]
    a = list(table.keys())
    b = list(table_2.keys())
    for key_2 in b:
        result[key_2] = table_2[key_2]
        for key_1 in a:
            if key_1 == key_2:
                result[key_1] = table[key_1] + table_2[key_2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list."""
    result: dict[str, int] = {}
    for i in values:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result