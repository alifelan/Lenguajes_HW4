def parseS(tokens: list):
    if tokens[0][1] != '(':
        raise SyntaxError('Invalid sequence')
    del tokens[0]
    if tokens[0][0] != 'OPERATOR':
        raise SyntaxError('Invalid sequence')
    del tokens[0]
    parseA(tokens)
    del tokens[0]
    parseA(tokens)
    if tokens[0][1] != ')':
        raise SyntaxError('Invalid sequence')
    del tokens[0]
    return true


def parseA(tokens:list)
    if tokens[0][1] == '(':
        parseS(tokens)
    else if tokens[0][1] != 'VARIABLE' && tokens[0][1] != 'NUMBER':
        raise SyntaxError('Invalid sequence')
