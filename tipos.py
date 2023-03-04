from enum import Enum

class TokenTypes(Enum):
    function = 0
    number = 1
    operator = 2
    parameters = 3
    string = 4

class Collection:
    functions = ['print', 'lowercase', 'uppercase']