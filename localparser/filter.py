
def filter(c: str)->int:
    """Return an id to the character received to acces the transition matrix.

    Args:
        c(str): Char to get id.

    Returns:
        int: ID of the character

    """
    if c.isdigit():
        return 0
    elif c.isalpha():
        return 1
    elif c == '$':
        return 2
    elif c in '()':
        return 3
    elif c == ' ':
        return 5
    elif c in '+-*/':
        return 4
    else:
        return 6
