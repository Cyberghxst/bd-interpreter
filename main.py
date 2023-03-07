from interpreter import Interpreter

# The "code" itself.
code = '$send[Your message was sent.;$channel[ID;false];$guild[ID;false];false]'
# Functions "supposed" usage:
"""
$send[message;channelId;guildId;returnId]
$channel[Id;fetch?]
$guild[Id;fetch?]
"""

# Splitting code into tokens.
tokens = Interpreter.tokenize(code)

# Printing tokens
print(tokens)