from lexer import Reader

# The "code" itself.
code = '$send[Your message was sent.;$channelID;false]'

# Splitting code into tokens.
tokens = Reader.tokenize(code)

# Printing tokens
print(tokens)