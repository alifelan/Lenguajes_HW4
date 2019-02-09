from localparser.filter import filter

ERROR = 999

TRANSITION_MATRIX = (
    (1,     ERROR,  2,      104,    0,      105,    ERROR),
    (1,     ERROR,  ERROR,  102,    102,    102,    ERROR),
    (ERROR, 3,      ERROR,  ERROR,  ERROR,  ERROR,  ERROR),
    (3,     3,      ERROR,  103,    103,    103,    ERROR)
)

TOKENS_NAMES = {
    102: 'NUMBER',
    103: 'VARIABLE',
    104: 'PARENTHESIS',
    105: 'OPERATOR'
}


def scan(s: str)-> list:
    """Return tokens given a string.

    Parses a string using the transition matrix and returns a list of tokens.

    Args:
        s(str): String parse

    Returns:
        list: List of strings with tokens names.

    """
    tokens: list = []
    state: int = 0
    value: str = ''
    for c in s:
        state = TRANSITION_MATRIX[state][filter(c)]
        if 100 > state != 0 or state == 104 or state == 105:
            value += c
        if state == 999:
            raise SyntaxError('Invalid token')
        if state > 100:
            tokens.append((TOKENS_NAMES[state], value))
            if state == 102 or state == 103:
                state = TRANSITION_MATRIX[0][filter(c)]
                if 100 > state != 0:
                    value = c
                if state == 999:
                    raise SyntaxError('Invalid token')
                if state > 100:
                    tokens.append((TOKENS_NAMES[state], c.strip()))
                    state = 0
                    value = ''
                value = c
            else:
                state = 0
                value = ''
    return tokens
