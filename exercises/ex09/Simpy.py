"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730466694"


class Simpy:
    """Defining my methods and constructors."""
    values: list[float]
    
    # TODO: Your constructor and methods will go here.
       
    def __init__(self, values: list[float]):
        """Initialization."""
        self.values = values

    def __str__(self) -> str:
        """Returns a string."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Fill Simpy's values with a specific number of repeating values."""
        self.values = [x] * y

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in values that attribute with range of values."""
        assert step != 0.0
        if start > stop:
            while start > stop:
                self.values.append(start)
                start += step
        else:
            while start < stop:
                self.values.append(start)
                start += step
                        
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return a new Simpy object and should not mutate the object the method is called on."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item + rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Returns exponentitation between two simpy objects at same indexes."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item ** rhs)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return equal items in two simpy objects at same indexes.""" 
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
            return result
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns items greater in a Simpy object at the same indexes.""" 
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
            return result
        else:
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
            return result
        
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Read specific items for Simpy."""
        if isinstance(rhs, int):
            if rhs < len(self.values):
                return self.values[rhs]
            else:
                raise IndexError
        else:
            result: list[float] = []
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.append(self.values[i])
                i += 1
            return Simpy(result)
        
