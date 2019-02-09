def parseS(tokens: list):
    if tokens[0][1] != '(':
        raise SyntaxError('Invalid sequence')
    del tokens[0]
    if tokens[0][0] != 'OPERATOR':
        raise SyntaxError('Invalid sequence')
    del tokens[0]
    parseA(tokens)
    parseA(tokens)
    if tokens[0][1] != ')':
        print(tokens[0][1])
        raise SyntaxError('Invalid sequence')
    del tokens[0]
    return True


def parseA(tokens: list):
    print("procesando" + tokens[0][1])
    if tokens[0][1] == '(':
        parseS(tokens)
    elif (tokens[0][0] != 'VARIABLE') and (tokens[0][0] != 'NUMBER'):
        raise SyntaxError('Invalid sequence')
    elif (tokens[0][0] == 'VARIABLE') or (tokens[0][0] == 'NUMBER'):
        del tokens[0]
