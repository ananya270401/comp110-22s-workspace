"""Exercise 6, Dictionary!"""

__author__ = "730466694"


def invert(inversion: dict[str, str]) -> dict[str, str]:
    """When given a key and value in dict[str, str], this function will invert the key and value values."""
    new_invert = {}
    for key, value in inversion.items():
        new_invert[value] = key
    return new_invert

    
def favorite_color(color: dict[str, str]) -> str:
    """When given a colors, it returns the most popular color."""  
    new_color = {}
    for key, value in color.items():
        if value in new_color:
            new_color[value] = new_color[value] + 1
        else:
            new_color[value] = 1
    colors = 0
    counter = 0
    for keys, value in new_color.items():
        if value > counter:
            colors = keys
            counter = value
    return(str(colors))
        

def count(number: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    counting: dict[str, int] = {}
    for key in number:
        if key in counting:
            counting[key] = counting[key] + 1
        else: 
            counting[key] = 1
    return counting