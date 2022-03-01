"""Example of a function that searches through a list."""


# Define a function nanesm contains
# Two parameters
# 1. needle - the string we're seraching for
# 2. haystack - th elist we're seraching through
def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West, Pete Davidson"]))
    

def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == '__main__':
    main()
else:
    print(__name__)
