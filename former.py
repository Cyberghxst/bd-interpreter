from tipos import Collection, TokenTypes

class Former:
    def form (tokens):
        length = len(tokens)
        pos = 0
        while pos < length:
            token = tokens[pos]
            if token.type == TokenTypes.function.name and token.value in Collection.functions:
                # More code
                pos += 2
            elif token.type == TokenTypes.string.name:
                # More code
                pos += 1
            else:
                raise Exception('ERROR: Unexpected token f{token.value}')