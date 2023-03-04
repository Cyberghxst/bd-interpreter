from tipos import TokenTypes

valid = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Reader:
    def tokenize (input, tokens = []):
        position = 0
        lines = input.split('\n') # Handling every enter.
        for line in lines: # Iterating every line
            while position < len(line):
                char = line[position]
                if char == '$':
                    position += 1
                    continue
                elif char in valid:
                    res = ''
                    while position < len(line) and line[position] != '[':
                        res += line[position]
                        position += 1
                    tokens.append({ "type": TokenTypes.function.name, "value": res })
                    continue
                elif char == '[':
                    args = ''
                    position += 1
                    while position < len(line) and line[position] != ']':
                        args += line[position]
                        position += 1
                    if position == len(line) and line[position] != ']':
                        raise Exception('ERROR: Expected "]" to close the function, but got nothing.')
                    params = args.split(';')
                    tokens.append({ "type": TokenTypes.parameters.name, "value": params })
                    continue
                elif char == ']':
                    position += 1
                    continue
                else:
                    raise Exception(f'ERROR: Unexpected identifier "{line[position]}"')
        return tokens